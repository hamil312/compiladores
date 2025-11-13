# Código generado automáticamente

def main():
    # Variables de usuario
    m = 0
    n = 0
    o = 0
    result = 0
    
    m = 0
    t0 = 0 - 1
    n = t0
    o = 2
    t1 = m != 1
    t2 = n + o
    t3 = t2 > 0
    t4 = o * 3
    t5 = t4 <= 6
    t6 = t3 or t5
    t7 = t1 and t6
    result = t7
    print(result)
    
    # Estado final de variables:
    try:
        print(f'm = {m}')
    except NameError:
        pass
    try:
        print(f'n = {n}')
    except NameError:
        pass
    try:
        print(f'o = {o}')
    except NameError:
        pass
    try:
        print(f'result = {result}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()