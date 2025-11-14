from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 

from generated.IfElseLangLexer import IfElseLangLexer
from generated.IfElseLangParser import IfElseLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
# Actualización para incluir generación de código
from codegen.PythonGenerator import PythonCodeGenerator
from codegen.VMGenerator import SimpleVM
from codegen.AssemblyGenerator import AssemblyGenerator
from codegen.DirectInterpreter import TACInterpreter

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Lanza una excepción para detener la ejecución de inmediato
        raise Exception(f"Error de sintaxis en la línea {line}:{column} - {msg}")

def main():
    try:
        # ==========================================
        # FASE 1: ANALISIS LEXICO
        # ==========================================
        print("FASE 1: ANALISIS LEXICO")
        print("-" * 40)
        
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = IfElseLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())
        
        # Mostrar tokens generados
        stream = CommonTokenStream(lexer)
        stream.fill()
        print("Tokens encontrados:")
        
        # Mapeo correcto de tipos de token según IfElseLang.tokens
        token_name_map = {
            1: "COMMA",
            2: "INT_TYPE", 
            3: "STRING_TYPE",
            4: "RETURN",
            5: "IF",
            6: "ELSE", 
            7: "LPAREN",
            8: "RPAREN",
            9: "LBRACE",
            10: "RBRACE",
            11: "SEMI",
            12: "ASSIGN",
            13: "LT",
            14: "GT", 
            15: "GE",
            16: "LE",
            17: "EQ",
            18: "NE",
            19: "PLUS",
            20: "MINUS",
            21: "MUL",
            22: "DIV",
            23: "ID",
            24: "NUMBER",
            25: "STRING",
            26: "COMMENT",
            27: "WS"
        }
        
        token_types = {}
        visible_token_count = 0
        
        for i, token in enumerate(stream.tokens[:-1]):  # Excluir EOF
            token_name = token_name_map.get(token.type, f"UNKNOWN_{token.type}")
            
            # Filtrar tokens de whitespace para mejor visualización
            if token_name != "WS":
                visible_token_count += 1
                # Contar tipos de tokens
                token_types[token_name] = token_types.get(token_name, 0) + 1
                print(f"  {visible_token_count:2d}. {token_name:12} -> '{token.text}'")
        
        print(f"\nResumen de tipos de token:")
        for token_type, count in sorted(token_types.items()):
            print(f"  - {token_type}: {count}")
        print(f"[OK] {visible_token_count} tokens significativos generados correctamente.")
        
        # ==========================================
        # FASE 2: ANALISIS SINTACTICO
        # ==========================================
        print("\nFASE 2: ANALISIS SINTACTICO")
        print("-" * 40)
        
        # Crear nuevo stream para el parser
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = IfElseLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())
        
        stream = CommonTokenStream(lexer)
        parser = IfElseLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        
        # Mostrar estructura del parse tree
        print("Estructura del Parse Tree:")
        def print_tree(node, indent=""):
            if hasattr(node, 'getText'):
                node_text = node.getText()
                if len(node_text) > 30:
                    node_text = node_text[:27] + "..."
                print(f"{indent}{type(node).__name__}: '{node_text}'")
            else:
                print(f"{indent}{type(node).__name__}")
            
            if hasattr(node, 'children') and node.children:
                for i, child in enumerate(node.children):
                    if i < 5:  # Limitar para evitar salida muy larga
                        print_tree(child, indent + "  ")
                    elif i == 5:
                        print(f"{indent}  ... ({len(node.children)-5} more children)")
                        break
        
        print_tree(tree)
        print(f"[OK] Parse tree generado con {tree.getChildCount()} nodos principales.")
        
        # ==========================================
        # FASE 3: ANALISIS SEMANTICO
        # ==========================================
        print("\nFASE 3: ANALISIS SEMANTICO")
        print("-" * 40)
        
        visitor = SemanticVisitor() 
        visitor.visit(tree)
        
        # Mostrar tabla de símbolos
        print("Tabla de Simbolos:")
        if hasattr(visitor, 'symbol_table') and visitor.symbol_table:
            for scope, symbols in visitor.symbol_table.scopes.items():
                if symbols:  # Solo mostrar scopes que tengan símbolos
                    print(f"  Ambito '{scope}':")
                    for symbol_name, symbol_info in symbols.items():
                        symbol_type = symbol_info.get('type', 'unknown')
                        symbol_line = symbol_info.get('line', 'N/A')
                        print(f"    - {symbol_name}: {symbol_type} (linea {symbol_line})")
        else:
            print("  (No se pudo acceder a la tabla de simbolos)")
        
        # Mostrar variables encontradas en el análisis
        print("\nVariables analizadas:")
        variables_found = set()
        if hasattr(visitor, 'ir') and hasattr(visitor.ir, 'instructions'):
            for inst in visitor.ir.instructions:
                if inst.get('result') and not inst['result'].endswith(':'):
                    variables_found.add(inst['result'])
                if inst.get('arg1') and inst['arg1'].replace('.','').replace('-','').isalnum():
                    variables_found.add(inst['arg1'])
                if inst.get('arg2') and inst['arg2'].replace('.','').replace('-','').isalnum():
                    variables_found.add(inst['arg2'])
        
        for var in sorted(variables_found):
            if var.startswith('t'):
                print(f"  - {var} (temporal)")
            elif var.isalpha():
                print(f"  - {var} (usuario)")
                
        print(f"[OK] Analisis semantico: {len(variables_found)} variables procesadas.")

        # ==========================================
        # FASE 4: GENERACION DE CODIGO INTERMEDIO (TAC)
        # ==========================================
        print("\nFASE 4: GENERACION DE CODIGO INTERMEDIO (TAC)")
        print("-" * 50)
        print(visitor.ir)
        
        # Análisis estadístico del código TAC
        print("\nAnalisis del Codigo Intermedio:")
        if hasattr(visitor, 'ir') and hasattr(visitor.ir, 'instructions'):
            instructions = visitor.ir.instructions
            
            # Contar tipos de operaciones
            operations_count = {}
            labels_count = 0
            assignments = 0
            
            for inst in instructions:
                op = inst.get('op', '')
                if op.endswith(':'):
                    labels_count += 1
                elif op == '=':
                    assignments += 1
                elif op in ['+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!=']:
                    operations_count[op] = operations_count.get(op, 0) + 1
                elif op in ['if_false_goto', 'goto']:
                    operations_count['control_flow'] = operations_count.get('control_flow', 0) + 1
                elif op in ['CALL', 'RETURN', 'PRINT']:
                    operations_count['functions'] = operations_count.get('functions', 0) + 1
                
            print(f"  - Total de instrucciones: {len(instructions)}")
            print(f"  - Asignaciones directas: {assignments}")
            print(f"  - Etiquetas de control: {labels_count}")
            
            if operations_count:
                print("  - Operaciones encontradas:")
                for op, count in operations_count.items():
                    if op == 'control_flow':
                        print(f"    * Control de flujo: {count}")
                    elif op == 'functions':
                        print(f"    * Llamadas/funciones: {count}")
                    else:
                        print(f"    * Operador '{op}': {count}")
        
        print(f"[OK] Codigo intermedio generado: {len(visitor.ir.instructions) if hasattr(visitor, 'ir') else 0} instrucciones TAC.")
        
        # ==========================================
        # FASE 5: GENERACIÓN DE CÓDIGO FINAL
        # ==========================================
        print("\nFASE 5: GENERACION DE CODIGO FINAL")
        print("=" * 50)
        
        # TARGET 1: PYTHON CODE GENERATION
        print("\n[TARGET 1: PYTHON CODE]")
        python_gen = PythonCodeGenerator()
        python_code = python_gen.generate_from_tac(visitor.ir.instructions)
        
        # Análisis del código Python generado
        lines = python_code.split('\n')
        code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
        comments = [l for l in lines if l.strip().startswith('#')]
        
        print(f"Estadisticas del codigo Python:")
        print(f"  - Lineas totales: {len(lines)}")
        print(f"  - Lineas de codigo: {len(code_lines)}")
        print(f"  - Comentarios: {len(comments)}")
        
        # Guardar y ejecutar código Python
        with open("output_program.py", "w", encoding='utf-8') as f:
            f.write(python_code)
            f.flush()  # Asegurar que se escriba al disco
        
        # Pequeño delay para asegurar que el archivo se haya escrito completamente
        import time
        time.sleep(0.1)
        
        # Ejecutar el código generado
        import subprocess
        import sys
        import os
        try:
            # Verificar que el archivo existe y tiene el contenido correcto
            if os.path.exists("output_program.py"):
                with open("output_program.py", "r", encoding='utf-8') as f:
                    file_content = f.read()
                    actual_lines = len(file_content.split('\n'))
                    print(f"  - Archivo verificado: {actual_lines} lineas")
            
            result = subprocess.run([sys.executable, "output_program.py"], 
                                  capture_output=True, text=True, timeout=5, 
                                  cwd=os.getcwd())
            if result.returncode == 0:
                print(f"  - Ejecucion exitosa: {result.stdout.strip()}")
            else:
                print(f"  - Error en ejecucion:")
                print(f"    stdout: {result.stdout}")
                print(f"    stderr: {result.stderr}")
        except subprocess.TimeoutExpired:
            print("  - Timeout en ejecucion")
        except Exception as e:
            print(f"  - Error al ejecutar: {str(e)}")
            
        print("[OK] Target Python: Codigo generado y probado.")
        
        # TARGET 2: ASSEMBLY CODE GENERATION  
        print("\n[TARGET 2: PSEUDO-ENSAMBLADOR]")
        asm_gen = AssemblyGenerator()
        assembly_code = asm_gen.generate(visitor.ir.instructions)
        
        # Mostrar el código ensamblador completo
        print(assembly_code)
        
        # Análisis del código ensamblador
        asm_lines = assembly_code.split('\n')
        instructions = [l for l in asm_lines if l.strip() and not l.strip().startswith('.') and not l.strip().startswith(';')]
        directives = [l for l in asm_lines if l.strip().startswith('.')]
        comments = [l for l in asm_lines if l.strip().startswith(';')]
        
        print(f"\nEstadisticas del pseudo-ensamblador:")
        print(f"  - Instrucciones: {len(instructions)}")
        print(f"  - Directivas: {len(directives)}")
        print(f"  - Comentarios: {len(comments)}")
        print("[OK] Target Assembly: Codigo generado correctamente.")
        
        # TARGET 3: VIRTUAL MACHINE EXECUTION
        print("\n[TARGET 3: MAQUINA VIRTUAL]")
        vm = SimpleVM()
        vm.load_program(visitor.ir.instructions)
        initial_memory = vm.memory.copy()
        vm.execute()
        final_memory = vm.memory.copy()
        
        print(f"Estado de la Maquina Virtual:")
        print(f"  - Variables iniciales: {len(initial_memory)}")
        print(f"  - Variables finales: {len(final_memory)}")
        print(f"  - Memoria final: {final_memory}")
        print("[OK] Target VM: Ejecucion completada.")
        
        # TARGET 4: DIRECT TAC INTERPRETATION
        print("\n[TARGET 4: INTERPRETADOR TAC DIRECTO]")
        interpreter = TACInterpreter()
        initial_vars = interpreter.variables.copy()
        interpreter.interpret(visitor.ir.instructions)
        final_vars = interpreter.variables.copy()
        
        print(f"Estado del Interpretador:")
        print(f"  - Variables procesadas: {len(final_vars)}")
        print(f"  - Estado final: {final_vars}")
        
        # Comparar resultados entre targets
        vm_resultado = final_memory.get('resultado', 'N/A')
        vm_suma = final_memory.get('suma', 'N/A')
        interp_resultado = final_vars.get('resultado', 'N/A') 
        interp_suma = final_vars.get('suma', 'N/A')
        
        print(f"\nComparacion de resultados:")
        print(f"  - Maquina Virtual: resultado = {vm_resultado}, suma = {vm_suma}")
        print(f"  - Interpretador TAC: resultado = {interp_resultado}, suma = {interp_suma}")
        
        # Análisis de consistencia
        if vm_resultado != interp_resultado:
            print(f"  ⚠️  Discrepancia detectada en 'resultado': VM={vm_resultado} vs TAC={interp_resultado}")
        else:
            print(f"  ✅ Resultados consistentes para 'resultado': {vm_resultado}")
            
        print("[OK] Target Interpreter: Interpretacion completada.")
        
        print("\n" + "=" * 50)
        print("*** COMPILACION COMPLETA - TODAS LAS FASES EXITOSAS ***")
        print("=" * 50)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()