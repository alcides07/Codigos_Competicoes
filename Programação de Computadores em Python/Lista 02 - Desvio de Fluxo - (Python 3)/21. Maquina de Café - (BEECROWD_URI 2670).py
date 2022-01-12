A1 = int(input()) 
A2 = int(input()) 
A3 = int(input()) 

Tempo_A1 = (A1 * 0) + (A2 * 2) + (A3 * 4)
Tempo_A2 = (A1 * 2) + (A2 * 0) + (A3 * 2)
Tempo_A3 = (A1 * 4) + (A2 * 2) + (A3 * 0)

if (Tempo_A1 <= Tempo_A2 and Tempo_A1 <= Tempo_A3):
    menor_tempo = Tempo_A1

elif (Tempo_A2 <= Tempo_A1 and Tempo_A2 <= Tempo_A3):
    menor_tempo = Tempo_A2

elif (Tempo_A3 <= Tempo_A1 and Tempo_A3 <= Tempo_A2):
    menor_tempo = Tempo_A3

print (menor_tempo)