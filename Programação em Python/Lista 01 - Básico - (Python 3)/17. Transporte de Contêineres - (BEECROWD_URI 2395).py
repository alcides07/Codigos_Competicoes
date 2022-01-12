A, B, C = map(int, input().split())  #A = LARGURA DO CONTÊINER. B = COMPRIMENTO DO CONTÊINER. C = ALTURA DO CONTÊINER
X, Y, Z = map(int, input().split())  #X = LARGURA DO NAVIO. Y = COMPRIMENTO DO NAVIO. Z = ALTURA MÁXIMA DA CARGA DO NAVIO.
max_conteiners = (X//A) * (Y//B) * (Z//C)

print(max_conteiners)