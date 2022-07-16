Tempo_Gasto = int(input())
Velocidade_Media = int(input())

Distancia_Percorrida = Velocidade_Media * Tempo_Gasto
Litros_necessarios = Distancia_Percorrida/12

print("{:.3f}".format(Litros_necessarios))