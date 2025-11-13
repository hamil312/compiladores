# Código generado automáticamente

def xor(a, b):
    # Variables temporales
    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    
    t0 = b == 0
    t1 = a and t0
    t2 = a == 0
    t3 = t2 and b
    t4 = t1 or t3
    return t4

def main():
    # Variables de usuario
    result = 0
    u = 0
    v = 0
    
    u = 1
    v = 0
    t5 = xor(u, v)
    t6 = u and v
    t7 = t5 or t6
    result = t7
    print(result)
    
    # Estado final de variables:
    try:
        print(f'result = {result}')
    except NameError:
        pass
    try:
        print(f'u = {u}')
    except NameError:
        pass
    try:
        print(f'v = {v}')
    except NameError:
        pass
    return 0

if __name__ == '__main__':
    main()