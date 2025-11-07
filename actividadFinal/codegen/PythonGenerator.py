class PythonCodeGenerator:
    def __init__(self):
        self.code_lines = []
        self.indent_level = 0

    def generate_from_tac(self, tac_instructions):
        """Genera código Python desde TAC, reconstruyendo if/while estructurados."""
        instrs = tac_instructions
        n = len(instrs)

        # mapa etiqueta -> índice
        label_map = {}
        for idx, inst in enumerate(instrs):
            op = inst.get('op')
            if isinstance(op, str) and op.endswith(':'):
                label_map[op[:-1]] = idx

        self.emit("# Código generado automáticamente")

        self.emit("def main():")
        self.indent()

        # declarar variables
        self.declare_variables(instrs)
        self.emit("")

        i = 0
        while i < n:
            inst = instrs[i]
            op = inst.get('op')

            # etiqueta: posible inicio de while
            if isinstance(op, str) and op.endswith(':'):
                label_name = op[:-1]
                # patrón while: LABEL, <cond assign>, if_false_goto <end>, ... body ..., goto LABEL, LABEL_end
                if i + 2 < n and instrs[i + 2].get('op') == 'if_false_goto':
                    # buscar goto de regreso a esta etiqueta en instrucciones posteriores
                    back_goto_idx = None
                    for j in range(i + 3, n):
                        if instrs[j].get('op') == 'goto' and instrs[j].get('result') == label_name:
                            back_goto_idx = j
                            break
                    end_label = instrs[i + 2].get('result')
                    end_idx = label_map.get(end_label)
                    if back_goto_idx is not None and end_idx is not None and end_idx > back_goto_idx:
                        # Emitir while recomputando la condición cada iteración:
                        # while True:
                        #     <cond_assignment>        # instrs[i+1]
                        #     if not <cond_operand>:  # instrs[i+2].arg1
                        #         break
                        #     <body>                  # instrs[i+3 .. back_goto_idx-1]
                        self.emit("while True:")
                        self.indent()
                        # emitir instrucción que calcula la condición (normalmente comparacion -> temp)
                        cond_assign_inst = instrs[i + 1]
                        code_cond = self.translate_instruction(cond_assign_inst)
                        if code_cond:
                            self.emit(code_cond)
                        cond_operand = instrs[i + 2].get('arg1')
                        # check and break if false
                        self.emit(f"if not {cond_operand}:")
                        self.indent()
                        self.emit("break")
                        self.dedent()
                        # cuerpo entre i+3 .. back_goto_idx-1
                        self._emit_range(instrs, i + 3, back_goto_idx)
                        self.dedent()
                        # saltar hasta la etiqueta end_idx + 1
                        i = end_idx + 1
                        continue
                # si no es while, simplemente avanzar (no emitir la etiqueta)
                i += 1
                continue

            # if / if-else detection: if_false_goto not part of while
            if op == 'if_false_goto':
                cond = inst.get('arg1')
                else_label = inst.get('result')
                else_idx = label_map.get(else_label)
                # buscar si después del then hay un goto a end_label (etiqueta después del else)
                # then starts at i+1
                # find index of label else_label (else_idx)
                if else_idx is None:
                    # fallback: emitir cond como linea cond check y seguir
                    self.emit(f"if {cond}:")
                    self.indent()
                    i += 1
                    continue

                # determinar posible end_label (si hay goto antes de else_label that jumps to end_label)
                # búsqueda de goto justo antes de else_idx
                then_end = else_idx  # exclusive
                possible_goto_idx = else_idx - 1
                has_end = False
                end_label = None
                end_idx = None
                if possible_goto_idx >= 0 and instrs[possible_goto_idx].get('op') == 'goto':
                    end_label = instrs[possible_goto_idx].get('result')
                    end_idx = label_map.get(end_label)
                    if end_idx is not None and end_idx > else_idx:
                        has_end = True

                # emitir if
                self.emit(f"if {cond}:")
                self.indent()
                # then block: from i+1 .. then_end-1 (exclude possible goto at end)
                then_block_end = possible_goto_idx if has_end else then_end
                self._emit_range(instrs, i + 1, then_block_end)
                self.dedent()

                if has_end:
                    # hay else
                    self.emit("else:")
                    self.indent()
                    # else block between else_idx+1 .. end_idx-1
                    self._emit_range(instrs, else_idx + 1, end_idx)
                    self.dedent()
                    i = end_idx + 1
                    continue
                else:
                    # no else: saltar a after else_label
                    i = else_idx + 1
                    continue

            # print / asignaciones / operaciones sencillas
            code = self.translate_instruction(inst)
            if code:
                self.emit(code)
            i += 1

        # imprimir estado final de variables
        user_variables = [v for v in sorted(self.get_all_variables(instrs)) if not v.startswith('t') and not v.startswith('L')]
        if user_variables:
            self.emit("")
            self.emit("# Estado final de variables:")
            for var in user_variables:
                self.emit(f"print(f'{var} = {{{var}}}')")
        else:
            self.emit("pass  # No hay variables de usuario para mostrar")

        self.emit("return 0")
        self.dedent()
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.emit("    main()")

        return '\n'.join(self.code_lines)

    # Helper que genera instrucciones lineales traducidas entre índices [start, end)
    def _emit_range(self, instrs, start, end):
        i = start
        while i < end and i < len(instrs):
            inst = instrs[i]
            # ignorar etiquetas porque se estructuraron
            if isinstance(inst.get('op'), str) and inst.get('op').endswith(':'):
                i += 1
                continue
            code = self.translate_instruction(inst)
            if code:
                self.emit(code)
            i += 1

    def translate_instruction(self, instruction):
        """Traduce una instrucción TAC a Python (lineal)."""
        op = instruction.get('op')

        if op in ['+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!=', 'and', 'or']:
            return f"{instruction.get('result')} = {instruction.get('arg1')} {op} {instruction.get('arg2')}"
        elif op == '=':
            return f"{instruction.get('result')} = {instruction.get('arg1')}"
        elif op == 'print':
            return f"print({instruction.get('arg1')})"
        # omitimos gotos y etiquetas aquí (se gestionan en la reconstrucción)
        return None

    def declare_variables(self, instructions):
        """Declara variables dentro de main()"""
        variables = self.get_all_variables(instructions)
        user_vars = [v for v in sorted(variables) if not v.startswith('t') and not v.startswith('L')]
        temp_vars = [v for v in sorted(variables) if v.startswith('t')]

        if user_vars:
            self.emit("# Variables de usuario")
            for var in user_vars:
                self.emit(f"{var} = 0")
        if temp_vars:
            self.emit("# Variables temporales")
            for var in temp_vars:
                self.emit(f"{var} = 0")

    def get_all_variables(self, instructions):
        variables = set()
        for inst in instructions:
            if inst.get('result') and isinstance(inst['result'], str):
                if not inst['result'].endswith(':'):
                    variables.add(inst['result'])
            if inst.get('arg1') and isinstance(inst['arg1'], str):
                if not inst['arg1'].lstrip('-').isdigit():
                    variables.add(inst['arg1'])
            if inst.get('arg2') and isinstance(inst['arg2'], str):
                if not inst['arg2'].lstrip('-').isdigit():
                    variables.add(inst['arg2'])
        return variables

    def emit(self, line):
        indent = "    " * self.indent_level
        self.code_lines.append(indent + line)

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1

    def dedent_if_needed(self):
        if self.indent_level > 1:
            self.dedent()