inicio, fim = map(int, input().split())

if (inicio == fim):
    duracao = 24

elif (inicio > fim):
    duracao = (24 - inicio) + fim

elif (fim > inicio):
    duracao = fim - inicio

print("O JOGO DUROU", duracao, "HORA(S)")