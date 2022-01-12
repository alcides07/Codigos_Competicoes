num = -1
while (num != 0):
    num = int(input())
    for i in range(1, num + 1):
        if (i == num):
            print(i)
        else:
            print(i, end = " ")