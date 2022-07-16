def divisores_rec(numero, divisor):
    if (divisor == 1):
        return [1]
    
    lista_divisores = divisores_rec(numero, divisor - 1)
    if (numero % divisor == 0):
        lista_divisores.append(divisor)
    return lista_divisores

num = int(input())
lista_formatada = divisores_rec(num, num)
print(*lista_formatada, sep = "\n")