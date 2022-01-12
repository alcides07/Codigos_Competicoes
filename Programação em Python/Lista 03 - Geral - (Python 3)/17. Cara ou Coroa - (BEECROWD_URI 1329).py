Num_Jogadas = -1
Qtd_Maria = 0
Qtd_Joao = 0

while (Num_Jogadas != 0):
    Num_Jogadas = int(input())
    if (Num_Jogadas == 0):
        break

    Sequencia_Jogadas = list(map(int, input().split()))
    Qtd_Maria = Sequencia_Jogadas.count(0)
    Qtd_Joao = Sequencia_Jogadas.count(1)
    print("Mary won {:d} times and John won {:d} times".format(Qtd_Maria, Qtd_Joao))