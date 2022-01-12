N_casos = int(input())

for i in range(0, N_casos):
    numero = int(input())
    qtd_div = 0
    for i in range(1, numero + 1):
        if (numero % i == 0):
            qtd_div += 1

    if (qtd_div == 2):
        print(numero, "eh primo")
    else:
        print(numero, "nao eh primo")