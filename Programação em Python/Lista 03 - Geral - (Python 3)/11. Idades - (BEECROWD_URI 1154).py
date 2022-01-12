idade = 0
lista_idades = []
contador = 0

while (idade >= 0):
    idade = int(input())
    if (idade >= 0):
        lista_idades.append(idade)
        contador += 1

print("{:.2f}".format(sum(lista_idades)/contador))