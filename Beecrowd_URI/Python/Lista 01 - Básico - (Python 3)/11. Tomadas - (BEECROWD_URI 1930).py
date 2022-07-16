T1,T2,T3,T4 = map(int,input().split())
Slot_1 = T1 - 1
Slot_2 = T2 - 1
Slot_3 = T3 - 1
Slot_4 = T4 
qtd_aparelhos = (Slot_1 + Slot_2 + Slot_3 + Slot_4) 

if (T1 >= 2 and T1 <= 6 and T2 >= 2 and T2 <= 6 and T3 >= 2 and T3 <= 6 and T4 >= 2 and T4 <= 6):
    print(qtd_aparelhos)
else:
    print("Algum dos valores fornecidos está fora do intervalo aceito (>= 2 e <= 6)")