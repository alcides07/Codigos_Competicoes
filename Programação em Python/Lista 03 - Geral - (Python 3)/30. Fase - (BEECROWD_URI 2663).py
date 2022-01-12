Num_Competidores = int(input())
Min_Classificados = int(input())
Qtd_Classificados = 0
Lista_Pontuacoes = []
Sub_Lista = []

for i in range(0, Num_Competidores):
    Pontuacao = int(input())
    Lista_Pontuacoes.append(Pontuacao)

Sub_Lista = sorted(set(Lista_Pontuacoes))
Tamanho_Nova_Lista = len(Sub_Lista)

for i in range(0, Tamanho_Nova_Lista):
    while (Qtd_Classificados < Min_Classificados):
        if (Lista_Pontuacoes.count(max(Sub_Lista)) >= 2):
            Qtd_Classificados += Lista_Pontuacoes.count(max(Sub_Lista))
            Sub_Lista.remove(max(Sub_Lista))
            
        elif (Lista_Pontuacoes.count(max(Sub_Lista)) == 1):
            if (Qtd_Classificados < Min_Classificados):
                Qtd_Classificados += 1
                Sub_Lista.remove(max(Sub_Lista))      
            else:
                break 

print(Qtd_Classificados)