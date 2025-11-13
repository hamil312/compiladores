# Código generado automáticamente

def both_true(a, b):
    # Variables temporales
    t0 = 0
    
    t0 = a and b
    return t0

def main():
    # Variables de usuario
    result = 0
    x = 0
    y = 0
    
    x = 1
    y = 1
    t1 = both_true(x, y)
    t2 = 0 == 0
    t3 = t1 and t2
    result = t3
    print(result)
    
    # Estado final de variables:
    try:
        print(f'result = {result}')
    except NameError:
        pass
    try:
        print(f'x = {x}')
    except NameError:
        pass
    try:
        print(f'y = {y}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()