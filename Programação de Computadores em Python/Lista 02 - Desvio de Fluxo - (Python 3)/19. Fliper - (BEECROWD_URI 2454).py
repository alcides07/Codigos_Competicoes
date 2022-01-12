P, R = map(int, input().split())

if (P == 0):
    resposta = "C"

elif (P == 1):
    if (R == 1):
        resposta = "A"
    elif (R == 0):
        resposta = "B"

print(resposta)