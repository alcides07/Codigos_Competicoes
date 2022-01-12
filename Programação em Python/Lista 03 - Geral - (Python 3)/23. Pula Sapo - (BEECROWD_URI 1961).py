def resultado(Altura_Pulo, Altura_Canos, Qtd_Canos):
    while (Qtd_Canos != 1):
        
        Cano_Atual = Altura_Canos[0] 
        Proximo_Cano = Altura_Canos[1] 

        Tem_Que_Pular = abs(Proximo_Cano - Cano_Atual)

        if (Tem_Que_Pular > Altura_Pulo):
            return ("GAME OVER")

        Altura_Canos = Altura_Canos[1:]
        Qtd_Canos = Qtd_Canos - 1

    return ("YOU WIN")

Altura_Pulo, Qtd_Canos = map(int, input().split())
Altura_Canos = list(map(int, input().split()))

print(resultado(Altura_Pulo, Altura_Canos, Qtd_Canos))