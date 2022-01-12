while True:
    try:
        Num_Casos = int(input())
        Lista_Velocidades = list(map(int, input().split()))
        Maior_Velocidade = max(Lista_Velocidades)

        if (Maior_Velocidade < 10):
            print("1")

        elif (Maior_Velocidade >= 10 and Maior_Velocidade < 20):
            print("2")

        else:
            print("3")
    
    except EOFError:
          break