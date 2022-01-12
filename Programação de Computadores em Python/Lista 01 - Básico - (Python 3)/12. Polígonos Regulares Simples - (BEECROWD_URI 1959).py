N, L = map(int, input().split())
Perimetro = N*L

if (N >= 3 and N <= 1000000 and L >= 1 and L <= 4000):
    print(Perimetro)
else:
    print("Algum dos valores fornecidos não está dentro da escala aceita!")