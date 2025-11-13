# Código generado automáticamente

def main():
    # Variables de usuario
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    result = 0
    
    a = 8
    b = 2
    c = 3
    d = 5
    e = 0
    t0 = b * c
    t1 = a + t0
    t2 = d - e
    t3 = t1 <= t2
    t4 = t3 == 0
    t5 = b > c
    t6 = e == 0
    t7 = t5 and t6
    t8 = t4 or t7
    result = t8
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
        print(f'e = {e}')
    except NameError:
        pass
    try:
        print(f'result = {result}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()