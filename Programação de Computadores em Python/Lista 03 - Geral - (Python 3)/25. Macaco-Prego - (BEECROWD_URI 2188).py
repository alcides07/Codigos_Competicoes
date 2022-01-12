Qtd_Regioes = -1
Num_Teste = 1

while (Qtd_Regioes != 0):
   Qtd_Regioes = int(input())

   if (Qtd_Regioes == 0):
      break

   xx = -12000
   xxx = 12000
   yy = 12000
   yyy = -12000

   for i in range(1, Qtd_Regioes + 1):
      X1, Y1, X2, Y2 = map(int, input().split())
      
      if (X1 > xx):
         xx = X1 

      if (X2 < xxx):
         xxx = X2 

      if (Y1 < yy):
         yy = Y1 

      if (Y2 > yyy):
         yyy = Y2 

   if (xx > xxx or yy < yyy):
      print("Teste {:d}\nnenhum\n".format(Num_Teste))

   else:
      print("Teste {:d}\n{:d} {:d} {:d} {:d}\n".format(Num_Teste, xx, yy, xxx, yyy))

   Num_Teste = Num_Teste + 1