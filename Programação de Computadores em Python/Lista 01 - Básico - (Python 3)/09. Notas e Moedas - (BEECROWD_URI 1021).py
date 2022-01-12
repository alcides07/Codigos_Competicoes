N = float(input()) 
notas = int(N)
moedas = int((N - notas) * 100)

print("NOTAS:")
N100 = N//100
resto = N%100
print(int(N100), "nota(s) de R$ 100.00")

N50 = resto//50
resto = N%50
print(int(N50), "nota(s) de R$ 50.00")

N20 = resto//20
resto = (N%50)%20
print(int(N20), "nota(s) de R$ 20.00")

N10 = resto//10
resto = N%10
print(int(N10), "nota(s) de R$ 10.00")

N5 = resto//5
resto = (N%10)%5
print(int(N5), "nota(s) de R$ 5.00")

N2 = resto//2
resto = (N%5)%2
print(int(N2), "nota(s) de R$ 2.00")

print("MOEDAS:")
print(int(resto), "moeda(s) de R$ 1.00")

N050 = moedas//50
print(int(N050), "moeda(s) de R$ 0.50")
resto = moedas%50

N025 = resto//25
resto = moedas%25
print(int(N025), "moeda(s) de R$ 0.25")

N10 = resto//10
resto = resto%10
print(int(N10), "moeda(s) de R$ 0.10")

N05 = resto//5
resto = moedas%5
print(int(N05), "moeda(s) de R$ 0.05")

N01 = resto//1
print(int(N01), "moeda(s) de R$ 0.01")