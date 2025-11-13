# Código generado automáticamente

def main():
    # Variables de usuario
    a = 0
    b = 0
    result = 0
    
    a = 0
    b = 3
    while a < 5:
        t1 = a + 1
        a = t1
    t2 = a == 5
    t3 = b < 10
    t4 = t2 and t3
    result = t4
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
        print(f'result = {result}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()