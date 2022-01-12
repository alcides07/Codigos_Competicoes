C, N = map(int,input().split())
T = C%N
if (C >= 1 and C <= 10**8):
    if (N >= 1 and N <= 100):
        print(T)
    else:
        print("Leonardo não costuma correr em uma pista com esse comprimento!")
else:
    print("Leonardo não pretende correr tanto assim!")
