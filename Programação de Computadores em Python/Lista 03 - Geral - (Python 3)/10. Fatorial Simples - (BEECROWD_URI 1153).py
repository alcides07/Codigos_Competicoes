def calc_fatorial(n):
    if(n == 0):
        return 1
    
    return n * calc_fatorial(n - 1)

num = int(input())
print(calc_fatorial(num))