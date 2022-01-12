a, g, ra, rg = map(float,input().split())
escolhido = ""

#a = preço do alcool
#g = preço da gasolina
#ra = rendimento alcool
#rg = rendimento gasolina

if (a == g):
    if(ra > rg):
        escolhido = "A"
    elif(rg > ra):
        escolhido = "G"
    elif(rg == ra):
        escolhido = "G"
    
if (a != g):
    if (((1 * 50)/ra) * a > ((1 * 50)/rg) * g):
        escolhido = "G"
    elif(((1 * 50)/ra) * a < ((1 * 50)/rg) * g):
        escolhido = "A"
    elif(((1 * 50)/ra) * a == ((1 * 50)/rg) * g):
        escolhido = "G"

print(escolhido)