P1, C1, P2, C2 = map(int, input().split()) #P1 e P2 = PESO DAS DUAS CRIANÇAS NA GANGORRA. C1 e C2 = COMPRIMENTO DOS DOIS LADOS DA GANGORRA.

if (P1 * C1 == P2 * C2): #A GANGORRA ESTÁ EQUILIBRADA QUANDO O PESO DAS DUAS CRIANÇAS E OS COMPRIMENTOS DOS DOIS LADOS DA GANGORRA SÃO IGUAIS.
    print("0")

elif (P1 * C1 < P2 * C2): #SE O LADO DIREITO DA GANGORRA É MAIOR E MAIS PESADO QUE O LADO ESQUERDO, A CRIANÇA DO LADO DIREITO ESTÁ NA PARTE DE BAIXO.
    print("1")

elif (P1 * C1 > P2 * C2): #SE O LADO ESQUERDO DA GANGORRA É MAIOR E MAIS PESADO QUE O LADO DIREITO, A CRIANÇA DO LADO ESQUERDO ESTÁ NA PARTE DE BAIXO.
    print("-1")
