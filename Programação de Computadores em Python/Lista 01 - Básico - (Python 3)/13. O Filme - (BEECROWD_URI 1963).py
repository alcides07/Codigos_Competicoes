A,B = map(float, input().split())
Aumento = ((B-A)/A)*100

if (A > 0.00 and B >= A and B <= 1000.00):
    print("{:.2f}%".format(Aumento))
else:
    print("Os valores fornecidos não estão dentro da escala aceita!")