N1, N2, N3, N4 = map(float, input().split())
Media_Ponderada = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/10  #Calculando média ponderada baseada nas 4 notas e em seus respectivos pesos

print("Media: {:.1f}".format(Media_Ponderada)) #Imprimindo a média ponderada com 1 casa decimal após o ponto.

if(Media_Ponderada >= 7.0):
    print("Aluno aprovado.")

elif(Media_Ponderada < 5.0):
    print("Aluno reprovado.")

elif(Media_Ponderada >= 5.0 and Media_Ponderada <= 6.9): #Todo o código abaixo representa algo semelhante a uma recuperação escolar.
    print("Aluno em exame.") 
    nota_exame_final = float(input()) #Pedindo do usuário a nota da recuperação
    print("Nota do exame:", nota_exame_final) 
 
    Media_Final = (Media_Ponderada + nota_exame_final)/2 #Recalculando a média baseada na nota da recuperação e na nota que o aluno tinha anteriormente.
    if(Media_Final >= 5.0): #Se o aluno foi aprovado na recuperação
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(Media_Final))
    elif (Media_Final <= 4.9): #Se o aluno foi reprovado na recuperação
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(Media_Final))