Lista_Senha = []
Num_Caso = 1

while (True):
    try:
        Qtd_Digitos = int(input())
        Lista_Oleosidades = list(map(float, input().split()))

        for i in range(0, Qtd_Digitos):
            Indice_Maior = Lista_Oleosidades.index(max(Lista_Oleosidades))
            Lista_Senha.append(Indice_Maior)
            Lista_Oleosidades.remove(max(Lista_Oleosidades))
            Lista_Oleosidades.insert(Indice_Maior, -1)

        print("Caso {:d}: ".format(Num_Caso), *Lista_Senha, sep = "")
        Num_Caso += 1

        Lista_Senha.clear()

    except EOFError:
        break