# Código generado automáticamente

def isGreater(x, y):
    # Variables temporales
    t0 = 0
    
    t0 = x > y
    return t0

def main():
    # Variables de usuario
    a = 0
    b = 0
    c = 0
    d = 0
    result = 0
    
    a = 10
    b = 4
    c = 7
    d = 1
    t1 = isGreater(a, b)
    t2 = isGreater(b, c)
    t3 = t1 or t2
    t4 = d == 0
    t5 = t4 == 0
    t6 = t3 and t5
    result = t6
    print(result)
    
    # Estado final de variables:
    try:
        print(f'a = {a}')
    except NameError:
        pass
    try:
        print(f'b = {b}')
    except NameError:
        pass
    try:
        print(f'c = {c}')
    except NameError:
        pass
    try:
        print(f'd = {d}')
    except NameError:
        pass
    try:
        print(f'result = {result}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()