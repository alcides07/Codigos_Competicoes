N = int(input())
A, B = map(int, input().split())

if(A + B <= N):
    print("Farei hoje!") #Se a soma do tempo dos dois presentes é menor ou igual ao tempo que o duende possui, então é possível ele fazer hoje.
else:
    print("Deixa para amanha!") #Se o tempo dos dois presentes juntos é maior que o tempo que o duende possui, então NÃO é possível ele fazer hoje, devendo deixar para amanhã.