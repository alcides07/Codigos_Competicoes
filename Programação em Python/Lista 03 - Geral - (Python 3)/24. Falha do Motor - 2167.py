Num_Medidas = int(input())
Lista_Medidas = list(map(int, input().split()))
Momento_Queda = 0

for i in range(1, len(Lista_Medidas)):
   if (Lista_Medidas[i] < Lista_Medidas[i - 1]):
      Momento_Queda = Lista_Medidas.index(Lista_Medidas[i]) + 1
      break

print(Momento_Queda)