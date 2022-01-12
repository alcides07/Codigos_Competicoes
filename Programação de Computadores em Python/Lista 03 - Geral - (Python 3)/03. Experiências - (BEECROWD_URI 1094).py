N_casos = int(input())
Total = 0
Total_Ratos = 0
Total_Sapos = 0
Total_Coelhos = 0

for i in range(0, N_casos):
    quantia, tipo = map(str, input().split())
    Total += int(quantia)
    if (tipo == "R"):
        Total_Ratos += int(quantia)
    if (tipo == "S"):
        Total_Sapos += int(quantia)
    if (tipo == "C"):
        Total_Coelhos += int(quantia)

print("Total: {:d} cobaias".format(Total))
print("Total de coelhos: {:d}".format(Total_Coelhos))
print("Total de ratos: {:d}".format(Total_Ratos))
print("Total de sapos: {:d}".format(Total_Sapos))
Total_Int = int(Total)
print("Percentual de coelhos: {:.2f}".format((Total_Coelhos*100)/Total_Int), "%")
print("Percentual de ratos: {:.2f}".format((Total_Ratos*100)/Total_Int), "%")
print("Percentual de sapos: {:.2f}".format((Total_Sapos*100)/Total_Int), "%")