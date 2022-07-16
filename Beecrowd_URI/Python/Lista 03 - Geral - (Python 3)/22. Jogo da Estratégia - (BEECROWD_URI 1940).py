Jogadores, Rodadas = map(int, input().split())
Entrada_Pontuacoes = list(map(int, input().split())) 

Slots_Pontos = [0] * Jogadores 

for i in range(Jogadores):
    Slots_Pontos[i] = sum(Entrada_Pontuacoes[i::Jogadores]) 

Slots_Pontos = Slots_Pontos[::-1]
Vencedor = Jogadores - Slots_Pontos.index(max(Slots_Pontos))

print(Vencedor)