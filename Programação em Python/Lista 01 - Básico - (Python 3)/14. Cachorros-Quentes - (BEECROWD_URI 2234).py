H, P = map(int, input().split())
Consumo_medio = H/P

if (H >= 1 and P <= 1000):
    print("{:.2f}".format(Consumo_medio))