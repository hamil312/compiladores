# Código generado automáticamente

def add(x, y):
    # Variables temporales
    t0 = 0
    
    t0 = x + y
    return t0

def isPositive(n):
    # Variables temporales
    t1 = 0
    
    t1 = n > 0
    return t1

def main():
    # Variables de usuario
    a = 0
    
    t2 = add(5, 3)
    a = t2
    print(a)
    t3 = isPositive(a)
    if t3:
        print(1)
    
    # Estado final de variables:
    try:
        print(f'a = {a}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()