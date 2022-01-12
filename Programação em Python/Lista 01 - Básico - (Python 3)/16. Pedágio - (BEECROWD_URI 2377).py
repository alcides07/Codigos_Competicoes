L, D = map(int, input().split())   #L = Comprimento da estrada.  D = Distância entre pedágios
K, P = map(int, input().split())   #K = Custo por quilômetro percorrido. P = Valor de cada pedágio
Qtd_Pedagios = L//D
Custo_Total_Pedagios = P*Qtd_Pedagios
Custo_Quilômetro = L*K

if(L >= 1 and D <= 10**4 and K>=1 and P <= 10**4):
    print(int(Custo_Total_Pedagios + Custo_Quilômetro))
else:
    print("Algum dos valores fornecidos não está dentro do conjunto aceito!")