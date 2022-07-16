Num_Pessoas = -1
Num_Teste = 0

while (Num_Pessoas != 0):
    Num_Teste += 1
    Num_Pessoas = int(input())

    if (Num_Pessoas != 0):
        lista_pessoas = list(map(int, input().split()))
        tamanho_lista = len(lista_pessoas)
        
        for i in range(0, tamanho_lista):
            if (lista_pessoas[i] == i + 1):
                print("Teste", Num_Teste)
                print(i + 1)
                print("")