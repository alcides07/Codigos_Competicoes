X_Maria, Y_Maria , X_Reuniao, Y_Reuniao = map(int,input().split())

Cruzamentos_X = abs(X_Reuniao - X_Maria) 

Cruzamentos_Y = abs(Y_Reuniao - Y_Maria)  

print(Cruzamentos_X + Cruzamentos_Y)