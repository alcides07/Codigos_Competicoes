Pessoas = int(input())
Lista = list(map(int, input().split()))

print(Lista.index(min(Lista)) + 1)