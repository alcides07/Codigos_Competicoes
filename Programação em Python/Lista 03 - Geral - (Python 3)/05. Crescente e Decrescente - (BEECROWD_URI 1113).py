x = 1
y = 0

while (x != y):
    x, y = map(int, input().split())
    if (x < y):
        print("Crescente")
    elif (x > y):
        print("Decrescente")