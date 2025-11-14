# codegen/PythonGenerator.py
class PythonCodeGenerator:
    def __init__(self):
        self.code_lines = []
        self.indent_level = 0
        
    def generate_from_tac(self, tac_instructions):
        """Genera código Python desde TAC"""
        self.emit("# Codigo generado automaticamente")
        self.emit("def main():")
        self.indent()
        
        # Declarar todas las variables usadas
        self.declare_variables(tac_instructions)
        self.emit("")
        
        # Traducir cada instrucción TAC
        for inst in tac_instructions:
            self.translate_instruction(inst)
            
        # Imprimir variables finales para debugging (detectar automáticamente)
        user_variables = [var for var in self.get_all_variables(tac_instructions) 
                         if not var.startswith('t') and not var.startswith('L')]
        
        if user_variables:
            # Mostrar las variables de usuario más relevantes
            for var in sorted(user_variables):
                self.emit(f"print(f'{var} = {{{var}}}')")
        else:
            self.emit("print('No user variables found')")
            
        self.emit("return 0")
        self.dedent()
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.emit("    main()")
        
        return '\n'.join(self.code_lines)
    
    def translate_instruction(self, instruction):
        """Traduce una instrucción TAC a Python"""
        op = instruction['op']
        
        if op in ['+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!=']:
            # t1 = a + b → t1 = a + b
            self.emit(f"{instruction['result']} = {instruction['arg1']} {op} {instruction['arg2']}")
            
        elif op == '=':
            # x = y → x = y
            self.emit(f"{instruction['result']} = {instruction['arg1']}")
            
        elif op == 'if_false_goto':
            # if_false t1 goto L1 → if t1 is true, execute next block, otherwise skip to L1
            self.emit(f"if {instruction['arg1']}:")
            self.indent()
            
        elif op == 'goto':
            # goto L1 → (usar excepciones o restructurar)
            self.emit(f"# goto {instruction['result']}")
            
        elif op.endswith(':'):
            # L1: → # L1:
            self.dedent_if_needed()
            self.emit(f"# {op}")
            
        elif op == 'CALL':
            # CALL func 2 → result = func(arg1, arg2)
            func_name = instruction['arg1']
            num_args = int(instruction['arg2']) if instruction['arg2'] else 0
            
            if instruction['result']:
                self.emit(f"{instruction['result']} = {func_name}()")
            else:
                self.emit(f"{func_name}()")
                
        elif op == 'RETURN':
            # RETURN value → return value
            if instruction['arg1']:
                self.emit(f"return {instruction['arg1']}")
            else:
                self.emit("return")
                
        elif op == 'PRINT':
            # PRINT value → print(value)
            self.emit(f"print({instruction['arg1']})")
    
    def declare_variables(self, instructions):
        """Declara todas las variables temporales y de usuario"""
        variables = set()
        
        for inst in instructions:
            # Procesar resultado de la instrucción
            if inst.get('result') and not inst['result'].endswith(':'):
                # Verificar que sea un identificador válido
                if inst['result'].isidentifier():
                    variables.add(inst['result'])
            
            # Procesar primer argumento
            if inst.get('arg1'):
                arg1 = str(inst['arg1'])
                # Solo agregar si es un identificador válido (variable, no literal)
                if arg1.isidentifier() and not arg1.isdigit():
                    variables.add(arg1)
            
            # Procesar segundo argumento
            if inst.get('arg2'):
                arg2 = str(inst['arg2'])
                # Solo agregar si es un identificador válido (variable, no literal)
                if arg2.isidentifier() and not arg2.isdigit():
                    variables.add(arg2)
        
        # Declarar variables en orden: primero las de usuario, luego las temporales
        user_vars = [var for var in sorted(variables) if not var.startswith('t') and not var.startswith('L')]
        temp_vars = [var for var in sorted(variables) if var.startswith('t')]
        label_vars = [var for var in sorted(variables) if var.startswith('L')]
        
        for var in user_vars + temp_vars + label_vars:
            self.emit(f"{var} = 0")
    
    def get_all_variables(self, instructions):
        """Extrae todas las variables de las instrucciones TAC"""
        variables = set()
        
        for inst in instructions:
            # Procesar resultado de la instrucción
            if inst.get('result') and not inst['result'].endswith(':'):
                if inst['result'].isidentifier():
                    variables.add(inst['result'])
            
            # Procesar argumentos (solo variables, no literales)
            for arg_key in ['arg1', 'arg2']:
                if inst.get(arg_key):
                    arg = str(inst[arg_key])
                    if arg.isidentifier() and not arg.isdigit():
                        variables.add(arg)
        
        return variables
    
    def emit(self, line):
        """Emite una línea con indentación apropiada"""
        indent = "    " * self.indent_level
        self.code_lines.append(indent + line)
    
    def indent(self):
        self.indent_level += 1
    
    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1
    
    def dedent_if_needed(self):
        """Reduce la indentación si estamos actualmente indentados (útil para etiquetas)"""
        if self.indent_level > 1:  # Mantener al menos 1 nivel para estar dentro de main()
            self.indent_level -= 1