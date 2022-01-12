N = int(input())
LA, LB = map(int, input().split())
SA, SB = map(int, input().split())

if (N <= LB and N <= SB and N >= LA and N >= SA): #A QUANTIDADE DE PEÇAS DE ROUPAS ESTÁ DENTRO DO INTERVALO ENTRE O MÍNIMO E O MÁXIMO TANTO DA LAVADORA QUANTO DA SECADORA
    print("possivel")

elif(N < LA): #A QUANTIDADE DE PEÇAS DE ROUPAS É MENOR QUE O MÍNIMO NECESSÁRIO NA LAVADORA
    print("impossivel")

elif(N > LB):
    print("impossivel") #A QUANTIDADE DE PEÇAS DE ROUPAS É MAIOR QUE O MÁXIMO SUPORTADO NA LAVADORA

elif(N > SB):
    print("impossivel") #A QUANTIDADE DE PEÇAS DE ROUPAS É MAIOR QUE O MÁXIMO SUPORTADO NA SECADORA

elif(N < SA):
    print("impossivel") #A QUANTIDADE DE PEÇAS DE ROUPAS É MENOR QUE O MÍNIMO NECESSÁRIO NA SECADORA