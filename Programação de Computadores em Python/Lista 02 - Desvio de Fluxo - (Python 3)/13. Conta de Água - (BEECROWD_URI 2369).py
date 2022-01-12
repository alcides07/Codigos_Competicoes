N = int(input())
preco_1 = 0
preco_2 = 0
preco_3 = 0

if(N >= 11):
    if(N >= 30):
        preco_1 = 1*20
    if(N < 30):
        preco_1 = 1* (N - 10)
        
if(N >= 31):
    if(N >= 100):
        preco_2 = 2*70

    if(N < 100):
        preco_2 = 2* (N - 30)

if(N >= 101):
    preco_3 = 5* (N - 100)

if(N >= 0 and N <= 10**3):
    print(preco_1 + preco_2 + preco_3 + 7)