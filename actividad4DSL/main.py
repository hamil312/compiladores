from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener
from semantic_analyzer.IR_Generator import IR_Generator
import json

NUMERIC_INT_FIELDS = {
    "Edad",
    "TiempoSegundos",
    "PosiciónFinal",
    "MejorVuelta",
    "PrimeraVuelta",
    "SegundaVuelta",
    "TerceraVuelta",
    "CuartaVuelta",
    "QuintaVuelta",
    "PenalizacionSegundos"
}

class AnalizadorCSV(CSVListener):
    def __init__(self):
        self.header = [] #Header donde se define la cabecera del CSV donde se determinan los nombres de la columna, se debe analizar aparte
        self.rows = []  # filas válidas como diccionarios
        self.duplicates_by_id = set()
        self.seen_corredor_ids = set()
        self.duplicate_rows_count = 0

        # Errores semánticos / de formato
        self.malformed_fields = []  # list of (line, field_name, raw_value, reason)
        self.missing_required = []  # list of (line, field_name)

        # Estadísticas/consultas
        self.best_time = None  # (time, row_dict)
        self.best_per_category = {}   # category -> (time, row_dict)
        self.best_per_country = {}    # country -> (time, row_dict)
        self.youngest = None  # (edad, row_dict)
        self.oldest = None    # (edad, row_dict)
        self.max_penalty = None  # (penalty, row_dict)
        self.ir = IR_Generator()
        self.header_assigned_externally = False
        self._first_row_skipped = False

        # Temporales para construir la fila actual (dependen de tu CSV.g4)
        # En general usaremos exitRow con ctx.field()
        # Si tu gramática llama a 'header' lo detectamos fuera.

    def _clean_field(self, raw):
        # Remueve comillas externas y espacios
        if raw is None:
            return ""
        s = raw.strip()
        if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
            s = s[1:-1]
        return s.strip()

    def exitRow(self, ctx:CSVParser.RowContext): #Este me genera dudas
        # Dependiendo de la gramática, las filas del header pueden venir como header.row()
        # Aquí asumimos que el caller (main) no pasa la cabecera a este listener
        fields = [self._clean_field(f.getText()) for f in ctx.field()]

        # Saltar header si ya fue asignado desde main()
        if self.header_assigned_externally and not self._first_row_skipped:
            self._first_row_skipped = True
            return

        # Si la cantidad de campos no coincide con la cabecera, lo marcamos
        if len(fields) != len(self.header):
            self.malformed_fields.append((ctx.start.line, "ROW_LENGTH", ",".join(fields), "cantidad_campos"))
            return

        row = dict(zip(self.header, fields))
        line_no = ctx.start.line

        # --- Detección de duplicados por CorredorID (suponemos existe la columna) ---
        corredor_id = row.get("CorredorID", "")
        if not corredor_id:
            self.missing_required.append((line_no, "CorredorID"))
            # No añadimos la fila
            return
        if corredor_id in self.seen_corredor_ids:
            self.duplicate_rows_count += 1
            self.duplicates_by_id.add(corredor_id)
            self.ir.add_instruction('ERROR_DUPLICADO', arg1=corredor_id)
            return
        self.seen_corredor_ids.add(corredor_id)

        # --- Validación y conversión de campos numéricos ---
        converted_row = dict(row)  # copia para convertir valores
        conversion_failed = False
        for field in NUMERIC_INT_FIELDS:
            conversion_failed = False 
            if field in row:
                raw = row[field]
                if raw == "" or raw is None:
                    # PosiciónFinal puede estar vacía (p.ej. descalificado). Lo aceptamos como None.
                    if field == "PosiciónFinal":
                        converted_row[field] = None
                        continue
                    # Si campo numérico vacío en general -> error semántico
                    self.malformed_fields.append((line_no, field, raw, "vacío"))
                    conversion_failed = True
                    continue
                # Normalizamos coma -> punto si existe (por si acaso)
                raw_norm = raw.replace(",", ".")
                try:
                    # todos los campos definidos como INT en este dataset, usamos int
                    iv = int(float(raw_norm))
                    converted_row[field] = iv
                except Exception as e:
                    self.malformed_fields.append((line_no, field, raw, "no_numérico"))
                    conversion_failed = True
                
                if conversion_failed:
                    self.ir.add_instruction('ERROR_CONVERSION', arg1=field, arg2=raw)
                else:
                    self.ir.add_instruction('CONVERT_INT', arg1=field, arg2=raw, result=str(converted_row[field]))

        # Convertir Descalificado
        descal = row.get("Descalificado", "").strip().lower()
        if descal in ("sí", "si", "s", "true", "yes"):
            converted_row["Descalificado"] = True
        elif descal in ("no", "n", "false", "0", ""):
            converted_row["Descalificado"] = False
        else:
            # valor inesperado
            converted_row["Descalificado"] = False
            self.malformed_fields.append((line_no, "Descalificado", row.get("Descalificado", ""), "valor_esperado Sí/No"))

        # Si conversion falló, guardamos la fila en rows igualmente para reporte,
        # pero no la consideramos para cálculos numéricos que requieran integridad
        self.rows.append(converted_row)

        # --- Estadísticas semánticas ---
        # Mejor tiempo global (ignora descalificados)
        if converted_row.get("Descalificado") is not True:
            t = converted_row.get("TiempoSegundos")
            if isinstance(t, int):
                if self.best_time is None or t < self.best_time[0]:
                    self.best_time = (t, converted_row)

        # Mejor por categoría
        cat = converted_row.get("Categoria")
        if cat:
            t = converted_row.get("TiempoSegundos")
            if isinstance(t, int):
                current = self.best_per_category.get(cat)
                if current is None or t < current[0]:
                    self.best_per_category[cat] = (t, converted_row)

        # Mejor por país
        pais = converted_row.get("Pais")
        if pais:
            t = converted_row.get("TiempoSegundos")
            if isinstance(t, int):
                self.ir.add_instruction('UPDATE_BEST_TIME', arg1=row['CorredorID'], arg2=t)
                current = self.best_per_country.get(pais)
                if current is None or t < current[0]:
                    self.best_per_country[pais] = (t, converted_row)

        # Youngest / Oldest (Edad)
        edad = converted_row.get("Edad")
        if isinstance(edad, int):
            if self.youngest is None or edad < self.youngest[0]:
                self.youngest = (edad, converted_row)
            if self.oldest is None or edad > self.oldest[0]:
                self.oldest = (edad, converted_row)

        # Max penalty
        pen = converted_row.get("PenalizacionSegundos")
        if isinstance(pen, int):
            if self.max_penalty is None or pen > self.max_penalty[0]:
                self.max_penalty = (pen, converted_row)

    def generate_ir(self):
        # Genera un JSON como representación intermedia (filas válidas)
        return {
            "rows": self.rows,
            "summary": {
                "duplicate_rows_count": self.duplicate_rows_count,
                "malformed_fields": self.malformed_fields,
                "best_time": self.best_time[1] if self.best_time else None,
                "best_per_category": {k: v[1] for k,v in self.best_per_category.items()},
                "best_per_country": {k: v[1] for k,v in self.best_per_country.items()},
                "youngest": self.youngest[1] if self.youngest else None,
                "oldest": self.oldest[1] if self.oldest else None,
                "max_penalty": self.max_penalty[1] if self.max_penalty else None
            }
        }

# main actualizado
def main():
    input_file = "races.csv"
    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    parser = CSVParser(stream)

    tree = parser.csvFile()  # parse completo

    # Camarilla: intentar extraer header desde el árbol si existe la regla header
    header = None
    try:
        header_ctx = tree.header()
        # header_ctx.row().field() -> lista de tokens
        header = [f.getText().strip().strip('"') for f in header_ctx.row().field()]
    except Exception:
        # fallback: leer la primera linea del archivo
        with open(input_file, "r", encoding="utf-8") as f:
            first = f.readline().strip()
            header = [h.strip() for h in first.split(",")]

    analizador = AnalizadorCSV()

    # Si prefieres que el listener no trate la primera fila como header,
    # fijamos header ya en el analizador para que skippee la primera fila
    analizador.header = header
    analizador.header_assigned_externally = True

    walker = ParseTreeWalker()
    walker.walk(analizador, tree)

    # Generar IR y guardarlo
    ir = analizador.generate_ir()
    with open("salida.json", "w", encoding="utf-8") as out:
        json.dump(ir, out, ensure_ascii=False, indent=2)

    # Imprimir resumen
    print("----- RESUMEN -----")
    print(f"Filas procesadas: {len(analizador.rows)}")
    print(f"Filas duplicadas por CorredorID: {analizador.duplicate_rows_count}")
    print("Campos malformados o vacíos (muestra):")
    for m in analizador.malformed_fields[:10]:
        print(" ", m)
    if analizador.best_time:
        print("Mejor tiempo global:", analizador.best_time[0], "Corredor:", analizador.best_time[1].get("CorredorID"))
    if analizador.best_per_category:
        print("Mejor por categoría:")
        for cat, (t, r) in analizador.best_per_category.items():
            print(" ", cat, "->", r.get("CorredorID"), t)
    if analizador.youngest:
        print("Más joven:", analizador.youngest[1].get("CorredorID"), "Edad:", analizador.youngest[0])
    if analizador.oldest:
        print("Más viejo:", analizador.oldest[1].get("CorredorID"), "Edad:", analizador.oldest[0])
    if analizador.max_penalty:
        print("Mayor penalización:", analizador.max_penalty[0], "Corredor:", analizador.max_penalty[1].get("CorredorID"))
    
    print("\n--- CÓDIGO INTERMEDIO (IR) ---")
    print(analizador.ir)

    print("## 🔤 TOKENS")
    for token in stream.tokens:
        if token.type != Token.EOF:
            print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

    print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
    parser = CSVParser(stream)
    tree = parser.csvFile()
    print(tree.toStringTree(recog=parser))

    def pretty_tree(node, rule_names, level=0):
        if isinstance(node, TerminalNode):
            return "  " * level + f"TOKEN({node.getText()})"
        else:
            rule_name = rule_names[node.getRuleIndex()]
            result = "  " * level + rule_name
            for child in node.children or []:
                result += "\n" + pretty_tree(child, rule_names, level + 1)
            return result

    print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
    print(pretty_tree(tree, parser.ruleNames))

if __name__ == "__main__":
    main()
    