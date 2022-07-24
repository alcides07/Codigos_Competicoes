def solve(y, x):
    if (y >= x):                  
        if (y % 2 == 0): 
            res = (y * y) - (x - 1)
        else:
            res = (y - 1) * (y - 1) + x
    
    else:
        if (x % 2 == 0):
            res = (x - 1) * (x - 1) + y 
        else:
            res = (x * x) - (y -  1)

    return res

casos = int(input())
for i in range(casos):
    y, x = map(int, input().split())
    print(solve(y, x))
