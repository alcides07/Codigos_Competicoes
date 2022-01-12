A, B, C = map(int, input().split())  #MÍNIMO 1 VIAGEM E NO MÁXIMO 3

if (A - B == 0 or A - C == 0 or B - C == 0): #Usou apenas 2 créditos - FOI X PARA O PASSADO, E FOI X PARA O FUTURO, OU VICE-VERSA. A MESMA QUANTIDADE.
    print("S")

elif (A + B == C or A + C == B or B + C == A): #Usou todos os 3 créditos - DOIS DOS VALORES JUNTOS SÃO IGUAIS A UM TERCEIRO, EQUIVALENDO A SER POSSÍVEL VOLTAR PARA O PRESENTE.
    print("S")

else: #Não é possível fazer no mínimo 1 viagem e no máximo 3, e ainda assim voltar para o presente.
    print("N")