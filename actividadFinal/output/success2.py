# Código generado automáticamente

def main():
    # Variables de usuario
    a = 0
    b = 0
    c = 0
    d = 0
    result = 0
    
    a = 5
    b = 3
    c = 2
    d = 0
    t0 = 0 - c
    t1 = b * t0
    t2 = a + t1
    t3 = t2 > 10
    t4 = d == 0
    t5 = 0 - 1
    t6 = b < t5
    t7 = t4 or t6
    t8 = t7 == 0
    t9 = t3 and t8
    result = t9
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