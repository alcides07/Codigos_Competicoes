Sequencia_Cartas = list(map(int, input().split()))
Situacao = ""
Passou_Crescente = False
Passou_Decrescente = False

for i in range(1, len(Sequencia_Cartas)):
    if (Sequencia_Cartas[i] > Sequencia_Cartas[i - 1]):
        Situacao = "C"
        Passou_Crescente = True
        
    elif (Sequencia_Cartas[i] < Sequencia_Cartas[i - 1]):
        Situacao = "D"
        Passou_Decrescente = True

    if (Passou_Crescente == True and Passou_Decrescente == True):
        Situacao = "N"

print(Situacao)