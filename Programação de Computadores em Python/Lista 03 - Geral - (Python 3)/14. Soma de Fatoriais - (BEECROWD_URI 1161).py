def fat(n1, n2):
    fat_1 = 1
    fat_2 = 1

    if (n1 == 0):
        fat_1 = 1

    if (n2 == 0):
        fat_2 = 1

    for x in range (1, n1):
        fat_1 = fat_1 * (x + 1)

    for i in range (1, n2):
       fat_2 = fat_2 * (i + 1)

    return fat_1 + fat_2

while True:
    try:
        n1, n2 = map(int, input().split())
        print(fat(n1, n2))
    except EOFError:
        break