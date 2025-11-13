# Código generado automáticamente

def main():
    # Variables de usuario
    a = 0
    b = 0
    c = 0
    result = 0
    
    a = 5
    b = 8
    c = 3
    t0 = a > 5
    t1 = b < 10
    t2 = t0 and t1
    t3 = c == 3
    t4 = t3 == 0
    t5 = t2 or t4
    result = t5
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
        print(f'result = {result}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()