from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 
import sys
import os
from io import StringIO

from generated.gramaticaLexer import gramaticaLexer
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonGenerator import PythonCodeGenerator

class DualWriter:
    """Escribe simultáneamente en consola y en archivo."""
    def __init__(self, file_handle, console):
        self.file = file_handle
        self.console = console
    
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
        self.file.flush()
    
    def flush(self):
        self.console.flush()
        self.file.flush()

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error de sintaxis en la línea {line}:{column} - {msg}")

def main():
    # Crear carpetas si no existen
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    # Buscar primer archivo .txt en la carpeta input/
    input_file = "input/failure13.txt"
    input_filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Generar nombres de salida
    output_py_file = os.path.join("output", f"{input_filename}.py")
    output_log_file = os.path.join("output", f"{input_filename}_file.txt")
    
    # Abrir archivo de salida
    output_log = open(output_log_file, "w", encoding='utf-8')
    
    # Redirigir stdout a dual writer (consola + archivo)
    original_stdout = sys.stdout
    sys.stdout = DualWriter(output_log, original_stdout)
    
    try:
        # ==========================================
        # FASE 1: ANALISIS LEXICO
        # ==========================================
        print("FASE 1: ANALISIS LEXICO")
        print("-" * 50)
        
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = gramaticaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())
        
        # Mostrar tokens generados
        stream = CommonTokenStream(lexer)
        stream.fill()
        print("Tokens encontrados:")
        
        # Mapeo actualizado para coincidir con tu gramática (desde gramaticaLexer)
        token_name_map = {
            1: "FUNCTION",
            2: "RETURN",
            3: "VAR",
            4: "INT_TYPE",
            5: "BOOL_TYPE",
            6: "AND",
            7: "OR",
            8: "NOT",
            9: "IF",
            10: "ELSE",
            11: "WHILE",
            12: "PRINT",
            13: "TRUE",
            14: "FALSE",
            15: "ASSIGN",
            16: "COLON",
            17: "COMMA",
            18: "SEMI",
            19: "LPAREN",
            20: "RPAREN",
            21: "LBRACE",
            22: "RBRACE",
            23: "ADD",
            24: "SUB",
            25: "MUL",
            26: "DIV",
            27: "EQ",
            28: "NEQ",
            29: "LTE",
            30: "GTE",
            31: "LT",
            32: "GT",
            33: "ID",
            34: "INT",
            35: "WS",
            36: "LINE_COMMENT",
            37: "BLOCK_COMMENT"
        }
        
        token_types = {}
        visible_token_count = 0
        
        for token in stream.tokens[:-1]:  # Excluir EOF
            token_name = token_name_map.get(token.type, f"UNKNOWN_{token.type}")
            
            if token_name != "WS":
                visible_token_count += 1
                token_types[token_name] = token_types.get(token_name, 0) + 1
                print(f"  {visible_token_count:2d}. {token_name:15} -> '{token.text}'")
        
        print("\nResumen de tipos de token:")
        for token_type, count in sorted(token_types.items()):
            print(f"  - {token_type}: {count}")
        print(f"[OK] {visible_token_count} tokens significativos generados.\n")
        
        # ==========================================
        # FASE 2: ANALISIS SINTACTICO
        # ==========================================
        print("FASE 2: ANALISIS SINTACTICO")
        print("-" * 50)
        
        parser = gramaticaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        
        print("Estructura del Parse Tree (primeros 50 caracteres por línea):")
        def print_tree(node, indent="", max_depth=6, current_depth=0):
            if current_depth > max_depth:
                return
            if hasattr(node, 'getText'):
                node_text = node.getText()
                if len(node_text) > 50:
                    node_text = node_text[:47] + "..."
                print(f"{indent}{type(node).__name__}: '{node_text}'")
            else:
                print(f"{indent}{type(node).__name__}")
            
            if hasattr(node, 'children') and node.children:
                for child in node.children:
                    print_tree(child, indent + "  ", max_depth, current_depth + 1)
        
        print_tree(tree)
        print(f"[OK] Parse tree generado correctamente.\n")
        
        # ==========================================
        # FASE 3: ANALISIS SEMANTICO
        # ==========================================
        print("FASE 3: ANALISIS SEMANTICO")
        print("-" * 50)
        
        visitor = SemanticVisitor()
        visitor.visit(tree)
        
        # Mostrar errores semánticos si hay
        if visitor.table.errors:
            print(f"\n⚠️  {len(visitor.table.errors)} error(es) semántico(s) encontrado(s):")
            for i, error in enumerate(visitor.table.errors, 1):
                print(f"  {i}. {error}")
            print()
        else:
            print("[OK] No se encontraron errores semánticos.\n")

        # Mostrar tabla de símbolos
        print("Tabla de Símbolos:")
        print("-" * 50)
        visitor.table.dump()
        print()
        
        # ✅ NUEVO: Si hay errores semánticos, abortar aquí
        if visitor.table.errors:
            print("[ABORT] No se puede continuar con errores semánticos.\n")
            return 1
                
        # ==========================================
        # FASE 4: GENERACION DE CODIGO INTERMEDIO
        # ==========================================
        print("FASE 4: GENERACION DE CODIGO INTERMEDIO (TAC)")
        print("-" * 50)
        
        if hasattr(visitor, 'ir') and visitor.ir.instructions:
            print(visitor.ir)
            print(f"[OK] {len(visitor.ir.instructions)} instrucciones TAC generadas.\n")
        else:
            print("Error: No se generó código intermedio.")
            print("[ABORT] No se puede continuar sin TAC.\n")
            return 1
        
        # ==========================================
        # FASE 5: GENERACION DE CODIGO PYTHON
        # ==========================================
        print("FASE 5: GENERACION DE CODIGO PYTHON")
        print("-" * 50)
        
        generator = PythonCodeGenerator()
        python_code = generator.generate_from_tac(visitor.ir.instructions, visitor.table)
        
        # Guardar código generado
        with open(output_py_file, "w") as f:
            f.write(python_code)
            
        print(f"Código Python generado y guardado en '{output_py_file}':\n")
        print("=" * 50)
        print(python_code)
        print("=" * 50)
        print(f"\n[OK] Generación de código completada.\n")
        
        # ==========================================
        # Resumen final
        # ==========================================
        print("RESUMEN DE COMPILACION")
        print("-" * 50)
        print(f"✓ Archivo de entrada:    {input_file}")
        print(f"✓ Análisis léxico:       {visible_token_count} tokens generados")
        print(f"✓ Análisis sintáctico:   Parse tree completado")
        print(f"✓ Análisis semántico:    {len(visitor.table.errors)} errores encontrados")
        print(f"✓ Código intermedio:     {len(visitor.ir.instructions)} instrucciones TAC")
        print(f"✓ Código Python:         Archivo '{output_py_file}' generado")
        print(f"✓ Log de compilación:    Archivo '{output_log_file}' generado")
        print("-" * 50)
        print("[SUCCESS] Compilación completada exitosamente.\n")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        return 1
    except Exception as e:
        error_msg = str(e)
        # Si es error de sintaxis de ANTLR, mostrar solo el mensaje limpio
        if "Error de sintaxis" in error_msg:
            print(f"\n❌ {error_msg}")
        else:
            # Para otros errores, mostrar traceback completo
            import traceback
            print("Error durante la compilación:")
            traceback.print_exc()
        print("[ABORT] Compilación abortada.\n")
        return 1
    finally:
        # Restaurar stdout y cerrar archivo
        sys.stdout = original_stdout
        output_log.close()
        print(f"[INFO] Salida guardada en '{output_log_file}'")

    return 0

if __name__ == '__main__':
    exit(main())