n1 = '1'
n2 = '1'

while (True):
    n1, n2 = input().split()
    if (n1 == '0' and n2 == '0'):
        break
   
    while (len(n1) > 1):
        Novo_N = 0

        for i in n1:
            Novo_N += int(i)
        n1 = str(Novo_N)
       
    while (len(n2) > 1):
        Novo_N2 = 0

        for i in n2:
            Novo_N2 += int(i)
            
        n2 = str(Novo_N2)

    if(int(n1) == int(n2)):
        print(0)
        
    elif(int(n1) > int(n2)):
        print(1)
        
    else:
        print(2)