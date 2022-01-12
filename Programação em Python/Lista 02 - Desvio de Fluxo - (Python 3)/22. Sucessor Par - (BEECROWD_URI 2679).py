X = int(input())
Proximo_Par = 0

if(X % 2 == 0): #SE O NÚMERO DIGITADO É PAR, O PRÓXIMO MENOR PAR DEPOIS DELE SE ENCONTRA 2 NÚMEROS DEPOIS.
     Proximo_Par = X + 2

elif(X % 2 != 0):
    Proximo_Par = X + 1 #SE O NÚMERO DIGITADO É ÍMPAR, O PRÓXIMO MENOR PAR DEPOIS DELE SE ENCONTRA 1 NÚMERO DEPOIS.

print(Proximo_Par)