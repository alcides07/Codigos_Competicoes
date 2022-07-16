A, B, C, D = map(int, input().split())

if (  A < B + C and A > abs(B - C)
      or  
      A < B + D and A > abs(B - D)
      or
      A < C + D and A > abs(C - D)
      or
      B < A + C and B > abs(A - C)
      or
      B < A + D and B > abs(A - D)
      or
      B < C + D and B > abs(C - D)
      or
      C < A + B and C > abs(A - B)
      or
      C < A + D and C > abs(A - D)
      or
      C < B + D and C > abs(B - D)
      or
      D < A + B and D > abs(A - B)
      or
      D < A + C and D > abs(A - C)
      or
      D < B + C and D > abs(B - C)
      ):
      print("S")

else:
    print("N")