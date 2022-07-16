x = int(input())
y = int(input())
menor = x
maior = y

if (y < x):
    menor = y
    maior = x
else:
    menor = x
    maior = y

for i in range(menor + 1,maior):
    if (i % 5 == 2 or i % 5 == 3):
        print(i)