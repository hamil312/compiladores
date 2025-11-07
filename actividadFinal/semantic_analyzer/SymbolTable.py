class Symbol:
    """
    Representa un símbolo en la tabla. Para este lenguaje manejamos variables
    (tipo 'int' o 'bool'). Se deja soporte básico para funciones por si se
    extiende la gramática.
    """
    def __init__(self, name, type=None, category='variable', params=None):
        self.name = name
        # type: 'int', 'bool', None (desconocido aún) o tipo de retorno si función
        self.type = type
        self.category = category  # 'variable' o 'function'
        self.params = params if params is not None else []

    def __str__(self):
        return f"<Symbol(name='{self.name}', type='{self.type}', category='{self.category}')>"

    __repr__ = __str__

class Scope:
    """
    Ámbito con su tabla de símbolos y enlace al scope envolvente.
    """
    def __init__(self, name, enclosing_scope=None):
        self.name = name
        self.symbols = {}
        self.enclosing_scope = enclosing_scope

    def insert(self, symbol):
        """Inserta un símbolo en este ámbito. Devuelve False si ya existe aquí."""
        if symbol.name in self.symbols:
            return False
        self.symbols[symbol.name] = symbol
        return True

    def lookup(self, name):
        """Busca en este ámbito; si no está, delega al padre."""
        symbol = self.symbols.get(name)
        if symbol:
            return symbol
        if self.enclosing_scope:
            return self.enclosing_scope.lookup(name)
        return None

    def defined_in_current_scope(self, name):
        """Chequea si un nombre está definido en este scope (no busca en padres)."""
        return name in self.symbols

    def list_symbols(self):
        return list(self.symbols.values())


class SymbolTable:
    """
    Gestión de la pila de ámbitos y utilidades para el analizador semántico.
    - Registra errores semánticos en self.errors (no hace sys.exit).
    - Permite declarar variables, asignarles tipos (inferir/verificar) y buscar símbolos.
    """
    def __init__(self):
        self.current_scope = Scope("global")
        self.errors = []

    def enter_scope(self, name="local"):
        """Entra a un nuevo scope anidado."""
        new_scope = Scope(name, enclosing_scope=self.current_scope)
        self.current_scope = new_scope

    def exit_scope(self):
        """Sale del scope actual (si existe un padre)."""
        if self.current_scope.enclosing_scope:
            self.current_scope = self.current_scope.enclosing_scope

    def record_error(self, msg):
        self.errors.append(msg)
        # También se puede imprimir para depuración:
        print("Semantic error:", msg)

    def define_var(self, name, var_type=None):
        """
        Declara una variable en el scope actual.
        - Si ya existe en el mismo scope, registra error y no sobrescribe.
        - var_type puede ser 'int' o 'bool' o None si se declara sin tipo.
        """
        if self.current_scope.defined_in_current_scope(name):
            self.record_error(f"El símbolo '{name}' ya está declarado en el ámbito '{self.current_scope.name}'.")
            return None
        sym = Symbol(name=name, type=var_type, category='variable')
        self.current_scope.insert(sym)
        return sym

    def set_var_type(self, name, var_type):
        """
        Asigna o verifica el tipo de una variable encontrada por lookup.
        - Si no existe, crea la variable en el scope actual (soporta definición implícita por asignación).
        - Si existe sin tipo, se le asigna.
        - Si existe con tipo distinto, registra error de incompatibilidad.
        """
        sym = self.lookup(name)
        if sym is None:
            # Creación implícita en el ámbito actual (p. ej. primera asignación)
            sym = Symbol(name=name, type=var_type, category='variable')
            self.current_scope.insert(sym)
            return sym

        if sym.category != 'variable':
            self.record_error(f"El símbolo '{name}' no es una variable.")
            return sym

        if sym.type is None:
            sym.type = var_type
            return sym

        # Ya tiene tipo: verificar compatibilidad
        if sym.type != var_type:
            self.record_error(f"Incompatibilidad de tipos para '{name}': {sym.type} vs {var_type}.")
        return sym

    def lookup(self, name):
        """Busca un símbolo en el scope actual y en los envolventes."""
        return self.current_scope.lookup(name)

    def define_function(self, name, return_type=None, params=None):
        """
        Método simple para declarar funciones (por si extiendes la gramática).
        Registra error si ya existe en el scope actual.
        """
        if self.current_scope.defined_in_current_scope(name):
            self.record_error(f"El símbolo '{name}' ya está declarado en el ámbito '{self.current_scope.name}'.")
            return None
        sym = Symbol(name=name, type=return_type, category='function', params=params or [])
        self.current_scope.insert(sym)
        return sym

    def get_errors(self):
        return self.errors[:]

    def dump(self):
        """Imprime todos los scopes desde el actual hacia el global (útil para debugging)."""
        s = self.current_scope
        levels = []
        while s:
            levels.append((s.name, {n: str(sym) for n, sym in s.symbols.items()}))
            s = s.enclosing_scope
        for name, syms in levels:
            print(f"Scope '{name}':")
            for n, desc in syms.items():
                print("  ", desc)