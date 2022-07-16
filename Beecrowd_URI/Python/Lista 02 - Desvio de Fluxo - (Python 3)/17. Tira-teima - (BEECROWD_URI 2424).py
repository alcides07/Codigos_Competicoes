X, Y = map(int, input().split()) #Coordenadas de contato da bola com o chão

if (X >= 0 and X <= 432 and Y >= 0 and Y <= 468 ):
    print("dentro")

else:
    print("fora")