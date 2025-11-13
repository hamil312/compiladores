# Código generado automáticamente

def main():
    # Variables de usuario
    result = 0
    x = 0
    y = 0
    z = 0
    
    x = 10
    y = 4
    z = 2
    t0 = y - z
    t1 = x / t0
    t2 = t1 >= 3
    t3 = y * z
    t4 = t3 == 8
    t5 = t4 == 0
    t6 = x < 20
    t7 = t5 and t6
    t8 = t2 or t7
    result = t8
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
    try:
        print(f'z = {z}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()