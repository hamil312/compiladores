from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener
from semantic_analyzer.IR_Generator import IR_Generator
import hashlib
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
} #Creamos un array con los campos enteros, esto nos permitirá verificar que tengan el valor correcto

class AnalizadorCSV(CSVListener):
    def __init__(self):
        self.header = [] #Header donde se define la cabecera del CSV donde se determinan los nombres de la columna, se debe analizar aparte
        self.rows = []  #Conjunto donde se almacenaran las filas a las que se puede aplicar el análisis
        self.duplicates_by_id = set() #Set para almacenar elementos con ID duplicadas
        self.seen_corredor_ids = set() #Set para almacenar elementos y realizar comparaciones, permitiendo hallar contenidos duplicados
        self.seen_row_hashes = set()  #Set para almacenar filas vistas y evitar filas idénticas (aunque ID difiera)
        self.duplicate_rows_content = []  #Guardar filas duplicadas por contenido
        self.duplicate_rows_count = 0 #Contador de valores duplicados

        self.malformed_fields = []  #Lista de campos malformados (linea, nombre del campo, valor crudo, razón)
        self.missing_required = []  #Lista de campos requeridos faltantes (linea, nombre del campo)

        self.best_time = None #Fila con el mejor tiempo (tiempo, fila)
        self.best_per_category = {} #Mejor por categoría diccionario (tiempo, fila)
        self.best_per_country = {} #Mejor por país diccionario (tiempo, fila)
        self.youngest = None #Participante más jóven (edad, fila)
        self.oldest = None #Participante de mayor edad (edad, fila)
        self.max_penalty = None #Penalización máxima alcanzada por un participante (penalización, fila)
        self.ir = IR_Generator() #Generador de representación intermedia
        self.header_assigned_externally = False #Variable boleana que verifica si se asignó la primera fila como header
        self._first_row_skipped = False #Variable boleana que verifica si se saltó el header se usan dos variables principalmente en caso de que llegue un csv sin header

    def _clean_field(self, raw): #Toma un campo en crudo y se deshace de elementos que dificulten el manejo del dato como pueden ser las comillas
        if raw is None: #Si el campo está vacio
            return "" #Retorna una cadena vacía
        s = raw.strip() #Extrae el elemento del campo, eliminando posibles whitespaces
        if len(s) >= 2 and s[0] == '"' and s[-1] == '"': #Verifica si el elemento esta rodeado de comillas
            s = s[1:-1] #Extrae solo los elementos ubicados entre las comillas
        return s.strip() #Retorna el elemento

    def exitRow(self, ctx:CSVParser.RowContext): #Función encargada del procesamiento de cada fila, recibe el contexto de las filas desde el CSVParser.py
        fields = [self._clean_field(f.getText()) for f in ctx.field()] #Se extraen los campos desde el contexto obtenido

        # Saltar header si ya fue asignado desde main()
        if self.header_assigned_externally and not self._first_row_skipped: #A través de main asignamos el header y modificamos la variable de esta clase que define si se asigno de forma externa, entonces este if verifica si ya se saltó la fila de la cabecera
            self._first_row_skipped = True #Si la primera fila del header no ha sido saltada y la cabecera ha sido asignada, entonces, se usa la variable boleana para saltar la fila y notificar a la clase que ya se saltó
            return #Procede a la siguiente fila

        # Si la cantidad de campos no coincide con la cabecera, lo marcamos
        if len(fields) != len(self.header): #Se toma la longitud de la fila, contando los campos y se la compara con la longitud del header, deben coincidir de otra forma la fila no está bien formada
            self.malformed_fields.append((ctx.start.line, "ROW_LENGTH", ",".join(fields), "cantidad_campos")) #Se añade a la lista de campos malformados, un elemento que incluye el inicio, es decir la posición del elemento en la tabla, ROW_Length (Que indica el error), La fila completa, y el mensaje cantidad_de_campos, de nuevo indicando el error
            return #Procede a la siguiente fila

        row = dict(zip(self.header, fields)) #Almacena la fila en un diccionario, agrupando el header con los campos de la fila actual, esto para determinar los valores y la columna a la que deben estar asignados 
        line_no = ctx.start.line #El número de la línea obtenido a través del contexto

        row_str = json.dumps(row, sort_keys=True, ensure_ascii=False)
        row_hash = hashlib.md5(row_str.encode('utf-8')).hexdigest()
        if row_hash in self.seen_row_hashes: #Si el row_hash se parece a uno de los que ya se han visto
            self.duplicate_rows_content.append((line_no, row)) #Se añade como una fila duplicada por su contenido
            self.ir.add_instruction('ERROR_DUPLICADO_CONTENIDO', arg1=str(row)) #Y se añade informa al IR sobre el error que se produjo
            return #Procede a la siguiente fila
        self.seen_row_hashes.add(row_hash) #Si no coincide con una fila ya existente se añade al conjunto

        #Detección de duplicados por CorredorID (suponemos existe la columna)
        corredor_id = row.get("CorredorID", "") #Toma el ID del corredor y lo almacena, de no existir el campo asigna una cadena vacía
        if not corredor_id: #Si no existe el ID del corredor
            self.missing_required.append((line_no, "CorredorID")) #Se agrega el campo a la lista de filas erroneas, añadiendo ambos el número de la línea y su ID
            # No añadimos la fila
            return #Pasamos a la siguiente fila
        if corredor_id in self.seen_corredor_ids: #Se busca si el ID se encuentra entre los IDs que ya se han visto
            self.duplicate_rows_count += 1 #Se aumenta el contador de filas duplicadas
            self.duplicates_by_id.add(corredor_id) #Se añade la ID del corredor al conjunto de IDs duplicadas
            self.ir.add_instruction('ERROR_DUPLICADO', arg1=corredor_id) #Se añade al generador de representación intermedia
            return #Pasamos a la siguiente fila
        self.seen_corredor_ids.add(corredor_id) #Se añade la ID a la lita de IDs que ya han aparecido

        #Validación y conversión de campos numéricos
        converted_row = dict(row) #Se realiza una copia de la fila a modificar, y se almacena en una variable
        conversion_failed = False #Se crea una variable para indicar si la conversión falló o fue exitosa
        for field in NUMERIC_INT_FIELDS: #Iteramos a través del conjunto de campos númericos y por cada uno verificamos el campo dentro de la fila actual
            conversion_failed = False #Se realiza esta asignación para reiniciar la variable, de otra forma se mostraría que la conversión falló incluso en casos exitosos
            if field in row: #Si se encuentra el campo en la fila
                raw = row[field] #Se almacena el campo sin modificar en una variable
                if raw == "" or raw is None: #Si el campo esta vacío
                    # PosiciónFinal puede estar vacía (p.ej. descalificado). Lo aceptamos como None.
                    if field == "PosiciónFinal": #Si el campo vacío es PosicionFinal
                        converted_row[field] = None #El campo se convierte en None
                        continue #Se continua el análisis de la fila
                    # Si campo numérico vacío en general -> error semántico
                    self.malformed_fields.append((line_no, field, raw, "vacío")) #Si el campo vacío no es PosiciónFinal, se procede a esta línea y se lo añade al conjunto de campos malformados
                    conversion_failed = True #Se confirma un fallo en la conversión
                    continue #Procedemos con la siguiente instrucción
                # Normalizamos coma -> punto si existe (por si acaso)
                raw_norm = raw.replace(",", ".") #Esta es la primera conversión, remplazando comas por puntos para normalizar el campo
                try:
                    # todos los campos definidos como INT en este dataset, usamos int
                    iv = int(float(raw_norm)) #Intentamos almacenar en una variable Int Value el número convertido a entero en caso de necesitarse
                    converted_row[field] = iv #Se añade el valor modificado al campo en el que corresponde en la fila
                except Exception as e: #En caso de un fallo (Como el número no siendo un número)
                    self.malformed_fields.append((line_no, field, raw, "no_numérico")) #Añadimos el campo fallido y su información al conjunto de campos mal formados y una explicación del error
                    conversion_failed = True #Notificamos del fallo en la conversión
                
                if conversion_failed: #En caso de fallar la conversión
                    self.ir.add_instruction('ERROR_CONVERSION', arg1=field, arg2=raw) #Notificamos del error al generador de representación intermedia
                else:
                    self.ir.add_instruction('CONVERT_INT', arg1=field, arg2=raw, result=str(converted_row[field])) #Notificamos de la conversión al generador de representación intermedia

        # Convertir Descalificado
        descal = row.get("Descalificado", "").strip().lower() #Tomamos el valor de la columna Descalificado, si no se encuentra se le asigna un valor vacío, strip se encarga de eliminar caracteres extra como espacios en blanco, lower convierte las letras en minusculas
        if descal in ("sí", "si", "s", "true", "yes"):
            converted_row["Descalificado"] = True
        elif descal in ("no", "n", "false", "0", ""):
            converted_row["Descalificado"] = False
        else:
            # valor inesperado
            converted_row["Descalificado"] = False
            self.malformed_fields.append((line_no, "Descalificado", row.get("Descalificado", ""), "valor_esperado Sí/No")) #Si se encuentra un valor inesperado se define que no hubo descalificación y se adjunta al conjunto de filas malformadas

        vueltas = [
            converted_row.get("PrimeraVuelta"),
            converted_row.get("SegundaVuelta"),
            converted_row.get("TerceraVuelta"),
            converted_row.get("CuartaVuelta"),
            converted_row.get("QuintaVuelta")
        ] #Conjunto de tiempos de cada vuelta de la fila actual
        penal = converted_row.get("PenalizacionSegundos", 0) #Obtenemos la penalización en segundos, de no existir asignamos 0

        if all(isinstance(v, int) for v in vueltas): #Si todas las vueltas son números enteros como debe ser
            tiempo_calculado = sum(vueltas) + (penal if isinstance(penal, int) else 0) #Se suma el tiempo en segundos de cada vuelta más la penalización si es valida
            tiempo_actual = converted_row.get("TiempoSegundos") #Obtenemos el tiempo total digitado

            if isinstance(tiempo_actual, int) and tiempo_actual != tiempo_calculado: #Si el tiempo actual es un entero y no es igual al tiempo calculado
                self.ir.add_instruction('CORRECCION_TIEMPO', arg1=row.get("CorredorID"), arg2=f"{tiempo_actual} -> {tiempo_calculado}") #Se notifica la corrección del tiempo al IR
                converted_row["TiempoSegundos"] = tiempo_calculado #Se asigna en la fila convertida el valor del tiempo correcto a la columna correspondiente

        # Si conversion falló, guardamos la fila en rows igualmente para reporte,
        # pero no la consideramos para cálculos numéricos que requieran integridad
        self.rows.append(converted_row) #Guardamos la fila convertida al conjunto de filas

        # --- Estadísticas semánticas ---
        # Mejor tiempo global (ignora descalificados)
        if converted_row.get("Descalificado") is not True: #Si el corredor no fue descalificado
            t = converted_row.get("TiempoSegundos") #Asignamos su tiempo a una variable
            if isinstance(t, int): #Verificamos que el tiempo sea una instancia de un número entero
                if self.best_time is None or t < self.best_time[0]: #Si aún no existe un mejor tiempo o el tiempo seleccionado es menor que el mejor tiempo actual
                    self.best_time = (t, converted_row) #Se añade a la fila actual y su tiempo como el mejor

        # Mejor por categoría
        cat = converted_row.get("Categoria") #Extraemos la categoria en una variable
        if cat: #Si hay un valor en el campo categoria
            t = converted_row.get("TiempoSegundos") #Obtenemos el tiempo total de la fila actual
            if isinstance(t, int): #Si el tiempo es correctamente un entero
                current = self.best_per_category.get(cat) #Obtenemos al mejor de la categoria determinada y lo asignamos a una variable
                if current is None or t < current[0]: #Si el actual no existe o el tiempo de la fila actual es menor que el del mejor de la categoria
                    self.best_per_category[cat] = (t, converted_row) #Actualizamos dicha categoria en el diccionario, asignando la fila actual como el mejor

        # Mejor por país
        pais = converted_row.get("Pais") #Obtenemos el país de la fila actual
        if pais: #Si se obtiene un valor para el país
            t = converted_row.get("TiempoSegundos") #Obtenemos el tiempo total de la fila actual
            if isinstance(t, int): #Si el tiempo es correctamente un entero
                self.ir.add_instruction('UPDATE_BEST_TIME', arg1=row['CorredorID'], arg2=t) #Se notifica al generador de representación intermedia que se actualizó el mejor tiempo
                current = self.best_per_country.get(pais) #Obtenemos al mejor del país determinado y lo asignamos a una variable
                if current is None or t < current[0]: #Si el actual no existe o el tiempo de la fila actual es menor que el del mejor del país
                    self.best_per_country[pais] = (t, converted_row) #Actualizamos dicho país en el diccionario, asignando la fila actual como el mejor

        # Youngest / Oldest (Edad)
        edad = converted_row.get("Edad") #Se obtiene y almacena el campo edad de la fila actual
        if isinstance(edad, int): #Si la edad es un entero de forma correcta
            if self.youngest is None or edad < self.youngest[0]: #Si aún no se define al más jóven o el corredor actual es más jóven
                self.youngest = (edad, converted_row) #Asignamos a la fila actual como el más jóven
            if self.oldest is None or edad > self.oldest[0]: #Si aún no se define al de mayor edad o el corredor actual es de mayor edad
                self.oldest = (edad, converted_row) #Asignamos a la fila actual como el corredor de mayor edad

        # Max penalty
        pen = converted_row.get("PenalizacionSegundos") #Obtenemos la penalización y la guardamos en una variable
        if isinstance(pen, int): #Verificamos que el valor obtenido sea un número entero
            if self.max_penalty is None or pen > self.max_penalty[0]: #Si aún no se ha definido una penalización máxima o la penalización de la fila actual es mayor
                self.max_penalty = (pen, converted_row) #Se asigna a la penalización como la máxima

    def generate_ir(self): #Encargada de generar la representación intermedia en un JSON
        return {
            "rows": self.rows, #Se muestran las filas
            "summary": { #El resúmen de los valores obtenidos durante el análisis
                "duplicate_rows_count": self.duplicate_rows_count, #Se muestra en el JSON la cantidad de filas duplicadas
                "duplicate_rows_by_content": len(self.duplicate_rows_content), #Se muestra la cantidad de filas duplicadas por contenido
                "malformed_fields": self.malformed_fields, #Se muestra en el JSON la cantidad de filas malformadas
                "best_time": self.best_time[1] if self.best_time else None, #Si existe un mejor tiempo se muestra, sino se muestra None
                "best_per_category": {k: v[1] for k,v in self.best_per_category.items()}, #Se muestra un conjunto, esto iterando a través de las claves y valores del conjunto de mejores por categoría
                "best_per_country": {k: v[1] for k,v in self.best_per_country.items()}, #Se muestra un conjunto, esto iterando a través de las claves y valores del conjunto de mejores por país
                "youngest": self.youngest[1] if self.youngest else None, #Si existe un corredor más jóven se muestra, sino se muestra None
                "oldest": self.oldest[1] if self.oldest else None, #Si existe un corredor de mayor edad se muestra, sino se muestra None
                "max_penalty": self.max_penalty[1] if self.max_penalty else None #Si existe una pena máxima se muestra, sino se muestra None
            }
        }

def main(): #Función principal donde se instancia el analizador y se realizan las operaciones necesarias
    input_file = "races.csv" #Seleccionamos el archivo csv a analizar
    input_stream = FileStream(input_file, encoding="utf-8") #Definimos el input_stream, que selecciona el formato que se utiliza para leer el archivo

    lexer = CSVLexer(input_stream) #Instanciamos el Lexer generado para nuestra gramática y le pasamos como argumento nuestro archivo
    stream = CommonTokenStream(lexer) #Usamos la clase de ANTLR4 para poder instanciar un Stream de tokens usando nuestro Lexer como parametro
    stream.fill() #Llenamos nuestor stream de tokens
    parser = CSVParser(stream) #Instanciamos nuestro parcer y le pasamos el stream como argumento

    tree = parser.csvFile() #Creamos el arbol sintáctico a través del parser

    header = None #Creamos una variable para header
    try:
        header_ctx = tree.header() #Intentamos extraer el header del arbol
        # header_ctx.row().field() -> lista de tokens
        header = [f.getText().strip().strip('"') for f in header_ctx.row().field()] #Actualizamos nuestra variable header obteniendo los valores de los campos en crudo del header tras aplicarles la función strip que elimina espacios extras y comillas
    except Exception: #Excepción en caso de fallos, se toma la primera fila como header
        with open(input_file, "r", encoding="utf-8") as f: #Abrimos el archivo en modo de lectura
            first = f.readline().strip() #Tomamos la primera linea
            header = [h.strip() for h in first.split(",")] #La dividimos en sus campos y les aplicamos strip

    analizador = AnalizadorCSV() #Instanciamos nuestro AnalizadorCSV

    analizador.header = header #Le informamos cual es el header a nuestro analizador
    analizador.header_assigned_externally = True #Notificamos a través de una variable que se ha realizado la asignación del header de forma externa

    walker = ParseTreeWalker() #A través de la clase de ANTLR4 generamos un walker que se encargará de caminar a través del arbol
    walker.walk(analizador, tree) #A travé de la función walk, recorremo el arbol usando el analizador

    ir = analizador.generate_ir() #Creamos una variable que almacene el JSON generado a través de generate_ir
    with open("salida.json", "w", encoding="utf-8") as out: #La función open abre un archivo o lo crea en caso de no existir, con el parametro w le decimos que queremos sobrescribir su contenido y definimos el formato, asignamos el resultado a out
        json.dump(ir, out, ensure_ascii=False, indent=2) #A través de la función dump, abrimos el archivo usando out y le escribimos el valor de ir, es decir nuestro JSON, el resto es formato

    # Imprimir resumen
    print("----- RESUMEN -----")
    print(f"Filas procesadas: {len(analizador.rows)}") #Imprimimos en pantalla la cantidad de filas validas que fueron procesadas
    print(f"Filas duplicadas por CorredorID: {analizador.duplicate_rows_count}") #Indicamos las filas duplicadas
    print(f"Filas duplicadas por contenido: {len(analizador.duplicate_rows_content)}") #Indicamos la cantidad de filas duplicadas por contenido
    print("Campos malformados o vacíos:") #Mostramos los campos malformados o vacíos
    for m in analizador.malformed_fields[:10]: #Por cada elemento en el conjunto de campos invalidos
        print(" ", m) #Se imprime el registro del campo
    if analizador.best_time: #Si existe el campo
        print("Mejor tiempo global:", analizador.best_time[0], "Corredor:", analizador.best_time[1].get("CorredorID")) #Se imprime el mejor tiempo y el corredor al que corresponde
    if analizador.best_per_category: #Si existen los mejores por categoría
        print("Mejor por categoría:") 
        for cat, (t, r) in analizador.best_per_category.items(): #Por cada categoría y su respectiva clave y valor entre los objetos almacenados en el diccionario de mejor por categoría
            print(" ", cat, "->", r.get("CorredorID"), t) #Se imprime la categoría, y se obtiene la id y el tiempo
    if analizador.youngest: #Si se definió un corredor más jóven
        print("Más joven:", analizador.youngest[1].get("CorredorID"), "Edad:", analizador.youngest[0]) #Se imprime el corredor más jóven obteniendo su ID y su edad
    if analizador.oldest:
        print("Más viejo:", analizador.oldest[1].get("CorredorID"), "Edad:", analizador.oldest[0])
    if analizador.max_penalty:
        print("Mayor penalización:", analizador.max_penalty[0], "Corredor:", analizador.max_penalty[1].get("CorredorID"))

    #print(analizador.ir)

    print("## 🔤 TOKENS")
    for token in stream.tokens: #Por cada token definido en el stream
        if token.type != Token.EOF: #Si el token no es un final de archivo
            print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}") #Se imprime el token

    print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
    print(tree.toStringTree(recog=parser)) #Imprimimos el arbol que hemos estado creando desde el inicio, primero como una cadena

    def pretty_tree(node, rule_names, level=0): #Una función que permite crear un arbol mejor organizado
        if isinstance(node, TerminalNode): #Se verifica si el nodo es un nodo terminal
            return "  " * level + f"TOKEN({node.getText()})" #Se retorna una cadena indentada según la cantidad de niveles del arbol, despues de los espacios se escribe el texto
        else:
            rule_name = rule_names[node.getRuleIndex()] #Si el nodo no es terminal se obtienen las reglas del nodo
            result = "  " * level + rule_name #El resultado es una oración indentada según la cantidad de niveles del arbol y que contiene el nombre de la regla
            for child in node.children or []: #Por cada nodo dentro del nodo
                result += "\n" + pretty_tree(child, rule_names, level + 1) #Se retorna como resultado la misma función a la que se le aplican las reglas y se le pasa el nodo hijo obtenido, además de aumentar el nivel para poder aumentar la indentación y mostrar el orden
            return result

    print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
    print(pretty_tree(tree, parser.ruleNames)) #Se usa la función para generar el arbol ordenado

if __name__ == "__main__":
    main() #Se ejecuta la función principal
    