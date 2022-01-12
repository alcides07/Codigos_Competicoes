Idade = int(input())
Ano = Idade//365
Meses = (Idade%365)//30
Dias = ((Idade%365)%30)

print(Ano, "ano(s)")
print(Meses, "mes(es)")
print(Dias, "dia(s)")