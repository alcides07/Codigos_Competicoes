N = int(input())

if (N > 0 and N < 1000000):
    print(N)
    N100 = N//100
    resto = N%100
    print(N100, "nota(s) de R$ 100,00")

    N50 = resto//50
    resto = N%50
    print(N50, "nota(s) de R$ 50,00")

    N20 = resto//20
    resto = (N%50)%20
    print(N20, "nota(s) de R$ 20,00")

    N10 = resto//10
    resto = N%10
    print(N10, "nota(s) de R$ 10,00")

    N5 = resto//5
    resto = (N%10)%5
    print(N5, "nota(s) de R$ 5,00")

    N2 = resto//2
    resto = (N%5)%2
    print(N2, "nota(s) de R$ 2,00")

    print(resto, "nota(s) de R$ 1,00")

else:
    print("O valor total digitado não está dentro dos limites aceitos!")