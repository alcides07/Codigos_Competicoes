9X, Y = map(float, input().split())

if (X == 0.0 and Y == 0.0):
    print("Origem") #Sobre a origem (0,0)

elif (X == 0.0 and Y != 0.0):
    print("Eixo Y") #Sobre o eixo Y (0, Y)

elif (Y == 0.0 and X != 0.0):
    print("Eixo X") #Sobre o eixo X (X, 0)

elif (X > 0.0 and Y > 0.0):
    print("Q1") #No primeiro quadrante

elif (X < 0.0 and Y > 0.0):
    print("Q2") #No segundo quadrante

elif (X < 0.0 and Y < 0.0):
    print("Q3") #No terceiro quadrante

elif (X > 0.0 and Y < 0.0):
    print("Q4") #No quarto quadrante