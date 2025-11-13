# Código generado automáticamente

def main():
    # Variables de usuario
    p = 0
    q = 0
    r = 0
    result = 0
    
    p = 7
    q = 7
    r = 1
    t0 = p == q
    t1 = q - r
    t2 = t1 <= 6
    t3 = t0 and t2
    t4 = t3 == 0
    t5 = t4 or 0
    result = t5
    print(result)
    
    # Estado final de variables:
    try:
        print(f'p = {p}')
    except NameError:
        pass
    try:
        print(f'q = {q}')
    except NameError:
        pass
    try:
        print(f'r = {r}')
    except NameError:
        pass
    try:
        print(f'result = {result}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()