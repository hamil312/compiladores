# Codigo generado automaticamente
def main():
    resultado = 0
    suma = 0
    x = 0
    y = 0
    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    L0 = 0
    L1 = 0
    
    x = 10
    y = 20
    t0 = x + y
    suma = t0
    t1 = suma > 25
    if t1:
        t2 = suma * 2
        resultado = t2
        # goto L1
    # L0:
    t3 = suma / 2
    resultado = t3
    # L1:
    print(f'resultado = {resultado}')
    print(f'suma = {suma}')
    print(f'x = {x}')
    print(f'y = {y}')
    return 0

if __name__ == '__main__':
    main()