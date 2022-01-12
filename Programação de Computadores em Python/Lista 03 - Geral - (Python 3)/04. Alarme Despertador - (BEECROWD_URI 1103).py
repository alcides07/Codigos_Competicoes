while True:
    Hora_At, Min_At, Hora_fin, Min_fin = map(int, input().split())
    if (Hora_At == Min_At == Hora_fin == Min_fin == 0):
        break

    else:
        Acordar = (Hora_fin * 60) + Min_fin
        Dormir = (Hora_At * 60) + Min_At

        if(Acordar < Dormir):
            Acordar += 24 * 60

    print(Acordar - Dormir)