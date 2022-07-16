codigo, qntd = map(int, input().split())
preco = 0

if(codigo == 1):
    preco = 4*qntd

elif(codigo == 2):
    preco = 4.50*qntd

elif(codigo == 3):
    preco = 5*qntd

elif(codigo == 4):
    preco = 2*qntd

elif(codigo == 5):
    preco = 1.50*qntd

print("Total: R$", "{:.2f}".format(preco))