v1, v2 = map(int, input().split())
tipo = ""

if (v2 >= 0 and v2 <= 2):
    tipo = "nova"

elif (v2 >= 3 and v2 <= 96):
    tipo = "crescente"

elif (v2 >= 97 and v2 <= 100):
    tipo = "cheia"

elif (v1 <= 100 and v1 > v2 and v2 <= 96 and v2 >= 3):
    tipo = "minguante"

print(tipo)