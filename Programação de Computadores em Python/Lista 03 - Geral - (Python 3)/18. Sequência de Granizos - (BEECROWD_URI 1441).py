def Granizo_Maior_Num(Num):
    return Num != 0 and ((Num & (Num - 1)) == 0)

while True:
    Num = int(input()) 
    
    if (Num == 0):
        break

    Maior_Numero = 0

    while (Granizo_Maior_Num(Num) != True):
        if (Num > Maior_Numero):
            Maior_Numero = Num

        if (Num % 2 == 0):
            Num = int(Num / 2)

        else:
            Num = (Num * 3) + 1

    if (Num > Maior_Numero):
        Maior_Numero = Num

    print(Maior_Numero)