ca, ba, pa = map(int, input().split()) #ca = frango > ba = bife > pa = massa
cr, br, pr = map(int, input().split()) #Quantidade de pessoas que quer cada um

frango_resultado = ca - cr
bife_resultado = ba - br
massa_resultado = pa - pr

if (frango_resultado > 0):
    frango_resultado = 0

if (bife_resultado > 0):
    bife_resultado = 0

if (massa_resultado > 0):
    massa_resultado = 0

print(-(bife_resultado + frango_resultado + massa_resultado))