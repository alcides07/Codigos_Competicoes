Qtd_Valores = int(input())
Lista_Num = []

for i in range(0, Qtd_Valores):
    Num = int(input())
    Lista_Num.append(Num)

Nova_Lista = sorted(set(Lista_Num))
Tamanho_Nova_Lista = len(Nova_Lista)

for i in range(0, Tamanho_Nova_Lista):
        print(Nova_Lista[i], "aparece", Lista_Num.count(Nova_Lista[i]), "vez(es)")