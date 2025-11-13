class PythonCodeGenerator:
    def __init__(self):
        self.code_lines = []
        self.indent_level = 0
        self.functions = {}  # dict para almacenar info de funciones
        self.current_function = None  # función actual siendo generada
        self.symbol_table = None  # opcional, inyectada desde main.py
        self._skip_until = -1  # índice hasta el que ya se emitió código (para evitar duplicados)

    def generate_from_tac(self, tac_instructions, symbol_table=None):
        """Genera código Python desde TAC, reconstruyendo if/while estructurados y funciones.
        Opcionalmente recibe la SymbolTable para obtener parámetros de funciones.
        """
        self.symbol_table = symbol_table

        instrs = tac_instructions
        n = len(instrs)

        # Mapeo etiqueta -> índice
        label_map = {}
        for idx, inst in enumerate(instrs):
            op = inst.get('op')
            if isinstance(op, str) and op.endswith(':'):
                label_map[op[:-1]] = idx

        # Primera pasada: identificar funciones (etiquetas func_<name> y end_func_<name>)
        self.extract_functions(instrs, label_map)

        # construir rangos de instrucciones que corresponden a funciones para poder saltarlas en main
        func_ranges = []
        for fn, info in self.functions.items():
            start = info.get('start_idx')
            end = info.get('end_idx')
            if start is not None and end is not None:
                func_ranges.append((start, end))

        # Generar código
        self.emit("# Código generado automáticamente")
        self.emit("")

        # Generar definiciones de funciones
        for func_name, func_info in self.functions.items():
            # obtener parámetros desde la symbol table si está disponible
            params = []
            if self.symbol_table:
                sym = self.symbol_table.lookup(func_name)
                if sym and sym.category == 'function':
                    params = [p[0] for p in sym.params]
            func_info['params'] = params
            self.generate_function(func_name, func_info, instrs, label_map)
            self.emit("")

        # Generar main
        self.emit("def main():")
        self.indent()

        # Declarar variables globales (excluyendo parametros de funciones)
        self.declare_variables(instrs)
        self.emit("")

        # Generar código principal (saltando funciones)
        i = 0
        while i < n:
            # si ya emitimos código hasta un índice, saltarlo
            if i <= self._skip_until:
                i = self._skip_until + 1
                continue
            # si la instrucción actual está dentro de un rango de función, saltar al final del mismo
            in_func = False
            for (s, e) in func_ranges:
                if s <= i <= e:
                    i = e + 1
                    in_func = True
                    break
            if in_func:
                continue

            inst = instrs[i]
            op = inst.get('op')
            
            # Saltar etiquetas sueltas
            if isinstance(op, str) and op.endswith(':'):
                i += 1
                continue
            
            # Procesar instrucción
            code = self.process_instruction(inst, instrs, i, label_map)
            if code:
                self.emit(code)
            i += 1

        # Imprimir estado final de variables
        # Excluir parámetros de funciones, nombres de funciones, temporales y etiquetas
        all_vars = sorted(self.get_all_variables(instrs))
        param_names = set()
        if self.symbol_table:
            global_syms = getattr(self.symbol_table.current_scope, "symbols", {})
            for name, sym in global_syms.items():
                if getattr(sym, "category", "") == "function":
                    for p in getattr(sym, "params", []):
                        param_names.add(p[0])

        user_variables = [
            v for v in all_vars
            if not (v.startswith('t') or v.startswith('L')
                    or v.startswith('func_') or v.startswith('end_func_')
                    or v in self.functions
                    or v in param_names)
        ]

        if user_variables:
            self.emit("")
            self.emit("# Estado final de variables:")
            # Emitir prints protegidos para evitar NameError si alguna variable no existe en tiempo de ejecución
            for var in user_variables:
                self.emit("try:")
                self.indent()
                self.emit(f"print(f'{var} = {{{var}}}')")
                self.dedent()
                self.emit("except NameError:")
                self.indent()
                self.emit("pass")
                self.dedent()
        else:
            self.emit("pass  # No hay variables de usuario para mostrar")

        self.emit("return 0")
        self.dedent()
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.emit("    main()")

        return '\n'.join(self.code_lines)

    def extract_functions(self, instrs, label_map):
        """Extrae información de funciones del TAC."""
        i = 0
        while i < len(instrs):
            op = instrs[i].get('op')
            if isinstance(op, str) and op.startswith('func_') and op.endswith(':'):
                func_name = op[5:-1]  # extrae nombre entre 'func_' y ':'
                end_label_name = f"end_func_{func_name}"
                end_idx = label_map.get(end_label_name)
                
                if end_idx is not None:
                    self.functions[func_name] = {
                        'start_idx': i,
                        'end_idx': end_idx,
                        'params': [],  # se llenará desde la symbol_table si existe
                        'return_var': None
                    }
            i += 1

    def generate_function(self, func_name, func_info, instrs, label_map):
        """Genera una función Python a partir de TAC."""
        self.current_function = func_name
        start_idx = func_info['start_idx']
        end_idx = func_info['end_idx']

        # Obtener parámetros (ya se cargaron en generate_from_tac)
        params = func_info.get('params', []) or []

        # Emitir definición de función con parámetros
        params_str = ", ".join(params)
        self.emit(f"def {func_name}({params_str}):")
        self.indent()

        # Declarar variables temporales locales (excluir parámetros)
        local_vars = self.get_function_variables(instrs, start_idx, end_idx)
        temp_vars = [v for v in sorted(local_vars) if v.startswith('t')]
        if temp_vars:
            self.emit("# Variables temporales")
            for var in temp_vars:
                self.emit(f"{var} = 0")

        self.emit("")
        return_val = None

        # Generar instrucciones de la función
        i = start_idx + 1  # saltar etiqueta func_
        while i < end_idx:
            inst = instrs[i]
            op = inst.get('op')

            # Saltar etiqueta final
            if isinstance(op, str) and op.endswith(':'):
                i += 1
                continue

            # Manejar return
            if op == 'ret':
                return_val = inst.get('arg1')
                self.emit(f"return {return_val}")
                i += 1
                continue

            # Procesar otra instrucción
            code = self.process_instruction(inst, instrs, i, label_map)
            if code:
                self.emit(code)
            i += 1

        self.dedent()
        self.current_function = None

    def process_instruction(self, inst, instrs, idx, label_map):
        """Procesa una instrucción TAC individual."""
        op = inst.get('op')

        # Operaciones binarias
        if op in ['+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!=', 'and', 'or']:
            return f"{inst.get('result')} = {inst.get('arg1')} {op} {inst.get('arg2')}"

        # Asignación
        elif op == '=':
            return f"{inst.get('result')} = {inst.get('arg1')}"

        # Print
        elif op == 'print':
            return f"print({inst.get('arg1')})"

        # Llamada a función
        elif op == 'call':
            func_name = inst.get('arg1')
            args = inst.get('arg2') or []
            args_str = ", ".join(map(str, args))
            result = inst.get('result')
            return f"{result} = {func_name}({args_str})"

        # Control de flujo (if/while reconstruidos en _process_control_flow)
        elif op == 'if_false_goto':
            return self._process_if(instrs, idx, label_map)

        # Return: solo emitir dentro de una función; fuera de funciones ignorar
        elif op == 'ret':
            if self.current_function:
                return f"return {inst.get('arg1')}"
            else:
                # ret fuera de función (no debería ocurrir si saltamos rangos), ignorar
                return None

        # Etiquetas (ignorar, ya procesadas)
        elif isinstance(op, str) and op.endswith(':'):
            return None

        # Gotos (ignorar, reconstruidos en if/while)
        elif op == 'goto':
            return None

        return None

    def _process_if(self, instrs, idx, label_map):
        """Procesa un if/if-else desde una instrucción if_false_goto."""
        inst = instrs[idx]
        cond = inst.get('arg1')
        else_label = inst.get('result')
        else_idx = label_map.get(else_label)

        if else_idx is None:
            self.emit(f"if {cond}:")
            self.indent()
            return None

        # Buscar goto antes de else_label
        then_end = else_idx
        possible_goto_idx = else_idx - 1
        has_else = False
        end_label = None
        end_idx = None

        if possible_goto_idx >= 0 and instrs[possible_goto_idx].get('op') == 'goto':
            end_label = instrs[possible_goto_idx].get('result')
            end_idx = label_map.get(end_label)
            if end_idx is not None and end_idx > else_idx:
                has_else = True

        # Emitir if
        self.emit(f"if {cond}:")
        self.indent()
        then_block_end = possible_goto_idx if has_else else then_end
        self._emit_range(instrs, idx + 1, then_block_end, label_map)
        self.dedent()

        if has_else:
            self.emit("else:")
            self.indent()
            self._emit_range(instrs, else_idx + 1, end_idx, label_map)
            self.dedent()

        # marcar hasta dónde ya emitimos para que el bucle principal lo salte
        skip_to = end_idx if end_idx is not None else then_block_end
        if isinstance(skip_to, int):
            self._skip_until = max(self._skip_until, skip_to)

        return None

    def _emit_range(self, instrs, start, end, label_map):
        """Emite un rango de instrucciones."""
        i = start
        while i < end and i < len(instrs):
            inst = instrs[i]
            op = inst.get('op')

            # Ignorar etiquetas
            if isinstance(op, str) and op.endswith(':'):
                i += 1
                continue

            code = self.process_instruction(inst, instrs, i, label_map)
            if code:
                self.emit(code)
            i += 1

    def declare_variables(self, instructions):
        """Declara variables dentro de main()."""
        variables = self.get_all_variables(instructions)
        # Construir conjunto de parámetros de todas las funciones (si hay symbol_table)
        param_names = set()
        if self.symbol_table:
            # buscar símbolos de funciones en el scope global
            global_scope = self.symbol_table.current_scope
            # recorrer símbolos y extraer params de funciones
            for name, sym in getattr(global_scope, "symbols", {}).items():
                if getattr(sym, "category", "") == "function":
                    for p in getattr(sym, "params", []):
                        param_names.add(p[0])

        # Excluir temporales y etiquetas y nombres de funciones y parámetros
        user_vars = [v for v in sorted(variables)
                    if not v.startswith('t')
                    and not v.startswith('L')
                    and not v.startswith('func_')
                    and not v.startswith('end_func_')
                    and v not in self.functions
                    and v not in param_names]

        if user_vars:
            self.emit("# Variables de usuario")
            for var in user_vars:
                self.emit(f"{var} = 0")

    def get_all_variables(self, instructions):
        """Extrae todas las variables del TAC."""
        variables = set()
        for inst in instructions:
            op = inst.get('op')
            # resultado: puede ser variable temporal/usuario o etiqueta de salto
            res = inst.get('result')
            if isinstance(res, str):
                # Si la instrucción es un salto, 'result' es etiqueta -> ignorar
                if op in ('goto', 'if_false_goto'):
                    pass
                else:
                    # evitar etiquetas nombradas y nombres de función
                    if not (res.startswith('L') or res.startswith('func_') or res.startswith('end_func_')):
                        variables.add(res)

            # arg1: en 'call' es el nombre de la función -> ignorar; else puede ser variable o literal
            a1 = inst.get('arg1')
            if isinstance(a1, str):
                if op == 'call':
                    # arg1 almacena el nombre de la función: no es variable
                    pass
                else:
                    if not a1.lstrip('-').isdigit() and a1 not in ('0', '1'):
                        variables.add(a1)

            # arg2: puede ser string o list (para call)
            a2 = inst.get('arg2')
            if isinstance(a2, str):
                if not a2.lstrip('-').isdigit() and a2 not in ('0', '1'):
                    variables.add(a2)
            elif isinstance(a2, list):
                for arg in a2:
                    if isinstance(arg, str) and not arg.lstrip('-').isdigit():
                        # evitar nombres de funciones si por error aparecen aquí
                        if not (arg.startswith('func_') or arg.startswith('end_func_')):
                            variables.add(arg)
        return variables

    def get_function_variables(self, instructions, start_idx, end_idx):
        """Extrae variables de una función específica."""
        variables = set()
        # obtener parámetros de esta función para excluirlos
        params = set()
        # intentar localizar nombre de la función y sus parámetros desde self.functions o symbol_table
        # buscamos función cuyo start_idx coincide
        for fname, info in self.functions.items():
            if info.get('start_idx') == start_idx:
                params = set(info.get('params', []))
                break
        # fallback a symbol_table
        if not params and self.symbol_table:
            # buscar símbolo por nombre
            for fname, info in self.functions.items():
                if info.get('start_idx') == start_idx:
                    sym = self.symbol_table.lookup(fname)
                    if sym:
                        params = set([p[0] for p in sym.params])
                        break

        for i in range(start_idx, end_idx + 1):
            inst = instructions[i]
            if inst.get('result') and isinstance(inst['result'], str):
                if not inst['result'].endswith(':') and inst['result'] not in params:
                    variables.add(inst['result'])
            a1 = inst.get('arg1')
            if isinstance(a1, str) and a1 not in params:
                if not a1.lstrip('-').isdigit() and a1 not in ('0', '1'):
                    variables.add(a1)
            a2 = inst.get('arg2')
            if isinstance(a2, str) and a2 not in params:
                if not a2.lstrip('-').isdigit() and a2 not in ('0', '1'):
                    variables.add(a2)
            elif isinstance(a2, list):
                for arg in a2:
                    if isinstance(arg, str) and arg not in params and not arg.lstrip('-').isdigit():
                        variables.add(arg)
        return variables

    def emit(self, line):
        """Emite una línea de código con indentación."""
        indent = "    " * self.indent_level
        self.code_lines.append(indent + line)

    def indent(self):
        """Aumenta indentación."""
        self.indent_level += 1

    def dedent(self):
        """Reduce indentación."""
        if self.indent_level > 0:
            self.indent_level -= 1