Diametro_Bola = int(input()) #Diâmetro da bola de boliche. Diâmetro = linha reta que, passando pelo centro, liga dois pontos de uma circunferência.
A, L, P = map(int, input().split()) #Altura, largura e profundidade da caixa

if (Diametro_Bola <= A and Diametro_Bola <= L and Diametro_Bola <= P): #Se o diâmetro da bola for menor que todas as medidas da caixa (altura, largura e profundidade), quer dizer que a bola cabe sim na caixa.
    print("S")

else: #Se o diâmetro da bola for maior do que qualquer uma das medidas da caixa, a bola não cabe nada caixa.
    print("N")