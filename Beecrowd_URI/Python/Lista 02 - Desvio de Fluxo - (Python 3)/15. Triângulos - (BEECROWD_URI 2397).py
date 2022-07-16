A, B, C = map(int, input().split())
Resposta = ""

if (A < B + C and A > abs(B - C)
      or  
      B < A + C and B > abs(A - C)
      or
      C < A + B and C > abs(A - B)):
      
    if (A > B and A > C):
        if (A**2 == B**2 + C**2):
            Resposta = "r"

        elif (A**2 > B**2 + C**2):
            Resposta = "o"

        elif (A**2 < B**2 + C**2):
            Resposta = "a"

    elif (B > A and B > C):
        if (B**2 == A**2 + C**2):
            Resposta = "r"

        elif (B**2 > A**2 + C**2):
            Resposta = "o"

        elif (B**2 < A**2 + C**2):
            Resposta = "a"

    elif (C > A and C > B):
        if (C**2 == A**2 + B**2):
            Resposta = "r"

        elif (C**2 > A**2 + B**2):
            Resposta = "o"

        elif (C**2 < A**2 + B**2):
            Resposta = "a"

    elif (A == B == C):
        if (A**2 < B**2 + C**2):
            Resposta = "a"

    print(Resposta)
    
else:
    print("n")