Num = int(input())
Sequencia_Fib = [0, 1]

for i in range(1, Num - 1):
        Proximo = Sequencia_Fib[i] + Sequencia_Fib[i - 1]
        if (Proximo != Num):
            Sequencia_Fib.append(Proximo)
        else:
            break
        
print(*Sequencia_Fib)