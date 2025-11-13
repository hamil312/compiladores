# Código generado automáticamente

def sum(x, y):
    # Variables temporales
    t0 = 0
    
    t0 = x + y
    return t0

def main():
    # Variables de usuario
    a = 0
    b = 0
    c = 0
    d = 0
    result = 0
    
    a = 2
    b = 7
    c = 5
    d = 12
    t1 = sum(a, b)
    t2 = t1 > c
    t3 = sum(b, c)
    t4 = t3 <= d
    t5 = t4 == 0
    t6 = t2 or t5
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