from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 

from generated.gramaticaLexer import gramaticaLexer
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonGenerator import PythonCodeGenerator

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error de sintaxis en la línea {line}:{column} - {msg}")

def main():
    try:
        # ==========================================
        # FASE 1: ANALISIS LEXICO
        # ==========================================
        print("FASE 1: ANALISIS LEXICO")
        print("-" * 40)
        
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = gramaticaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())
        
        # Mostrar tokens generados
        stream = CommonTokenStream(lexer)
        stream.fill()
        print("Tokens encontrados:")
        
        # Mapeo actualizado para coincidir con tu gramática
        token_name_map = {
            1: "AND",
            2: "OR", 
            3: "NOT",
            4: "IF",
            5: "ELSE",
            6: "WHILE",
            7: "PRINT",
            8: "TRUE",
            9: "FALSE",
            10: "ASSIGN",
            11: "SEMI",
            12: "LPAREN",
            13: "RPAREN",
            14: "LBRACE",
            15: "RBRACE",
            16: "ADD",
            17: "SUB",
            18: "MUL",
            19: "DIV",
            20: "EQ",
            21: "NEQ",
            22: "LTE",
            23: "GTE",
            24: "LT",
            25: "GT",
            26: "ID",
            27: "INT",
            28: "WS",
            29: "LINE_COMMENT",
            30: "BLOCK_COMMENT"
        }
        
        token_types = {}
        visible_token_count = 0
        
        for token in stream.tokens[:-1]:  # Excluir EOF
            token_name = token_name_map.get(token.type, f"UNKNOWN_{token.type}")
            
            if token_name != "WS":
                visible_token_count += 1
                token_types[token_name] = token_types.get(token_name, 0) + 1
                print(f"  {visible_token_count:2d}. {token_name:12} -> '{token.text}'")
        
        print("\nResumen de tipos de token:")
        for token_type, count in sorted(token_types.items()):
            print(f"  - {token_type}: {count}")
        print(f"[OK] {visible_token_count} tokens significativos generados.")
        
        # ==========================================
        # FASE 2: ANALISIS SINTACTICO
        # ==========================================
        print("\nFASE 2: ANALISIS SINTACTICO")
        print("-" * 40)
        
        parser = gramaticaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        
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
                for child in node.children:
                    print_tree(child, indent + "  ")
        
        print_tree(tree)
        print(f"[OK] Parse tree generado correctamente.")
        
        # ==========================================
        # FASE 3: ANALISIS SEMANTICO
        # ==========================================
        print("\nFASE 3: ANALISIS SEMANTICO")
        print("-" * 40)
        
        visitor = SemanticVisitor()
        visitor.visit(tree)
        
        # Mostrar errores semánticos si hay
        if visitor.table.errors:
            print("\nErrores semánticos encontrados:")
            for error in visitor.table.errors:
                print(f"  - {error}")
        else:
            print("[OK] No se encontraron errores semánticos.")

        # Mostrar tabla de símbolos
        print("\nTabla de Símbolos:")
        visitor.table.dump()
                
        # ==========================================
        # FASE 4: GENERACION DE CODIGO INTERMEDIO
        # ==========================================
        print("\nFASE 4: GENERACION DE CODIGO INTERMEDIO (TAC)")
        print("-" * 40)
        
        if hasattr(visitor, 'ir'):
            print(visitor.ir)
            print(f"[OK] {len(visitor.ir.instructions)} instrucciones TAC generadas.")
        else:
            print("Error: No se generó código intermedio.")
            return
        
        # ==========================================
        # FASE 5: GENERACION DE CODIGO PYTHON
        # ==========================================
        print("\nFASE 5: GENERACION DE CODIGO PYTHON")
        print("-" * 40)
        
        generator = PythonCodeGenerator()
        python_code = generator.generate_from_tac(visitor.ir.instructions)
        
        # Guardar código generado
        output_file = "output.py"
        with open(output_file, "w") as f:
            f.write(python_code)
            
        print(f"Código Python generado y guardado en '{output_file}':")
        print("-" * 40)
        print(python_code)
        print("-" * 40)
        print("[OK] Generación de código completada.")

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0

if __name__ == '__main__':
    main()