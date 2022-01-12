A, B, C = map(int, input().split())
H, L = map(int, input().split())

Menor_Dimensao_Colchao = 0
Segunda_Dimensao_Colchao = 0

Menor_Dimensao_Porta = 0
Maior_Dimensao_Porta = 0

if (H >= L):
    Maior_Dimensao_Porta = H
    Menor_Dimensao_Porta = L
else:
    Maior_Dimensao_Porta = L
    Menor_Dimensao_Porta = H

if (A >= B):
    if (A >= C):
        if (C >= B):
            Segunda_Dimensao_Colchao = C
            Menor_Dimensao_Colchao = B
        else:
            Segunda_Dimensao_Colchao = B
            Menor_Dimensao_Colchao = C
    else:
        Segunda_Dimensao_Colchao = A
        Menor_Dimensao_Colchao = B

elif (B >= A):
    if (B >= C):
        if (A >= C):
            Segunda_Dimensao_Colchao = A
            Menor_Dimensao_Colchao = C
        else:
            Segunda_Dimensao_Colchao = C
            Menor_Dimensao_Colchao = A
    else:
        Segunda_Dimensao_Colchao = B
        Menor_Dimensao_Colchao = A

elif (C >= A):
    if (C >= B):
        if (A >= B):
            Segunda_Dimensao_Colchao = A
            Menor_Dimensao_Colchao = B
        else:
            Segunda_Dimensao_Colchao = B
            Menor_Dimensao_Colchao = A
    else:
        Segunda_Dimensao_Colchao = C
        Menor_Dimensao_Colchao = A

if (Menor_Dimensao_Colchao <= Menor_Dimensao_Porta and Segunda_Dimensao_Colchao <= Maior_Dimensao_Porta):
    print ("S")

else:
    print("N")