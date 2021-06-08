def suma(valor1, valor2):
    return valor1 + valor2

def resta(valor1, valor2):
    return valor1 - valor2

def potencia(base, exponente):
    return base ** exponente

# 0 1 1 2 3 5 8 13 21 ....
def fibbo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        t1 = 0
        t2 = 1
        
        contador = 3
        
        while contador <= n:
            f = t1 + t2
            t1 = t2
            t2 = f
            contador += 1
            
        return f
