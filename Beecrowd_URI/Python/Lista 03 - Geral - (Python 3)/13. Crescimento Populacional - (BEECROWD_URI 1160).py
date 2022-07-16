n_Casos = int(input())
qtd_anos_passaram = 0
aumento_ano_a = 0
aumento_ano_b = 0

for i in range(1, n_Casos + 1):
    pop_a, pop_b, cresc_a, cresc_b = map(float, input().split())
    qtd_anos_passaram = 0

    while (pop_a <= pop_b):
        aumento_ano_a = (pop_a * cresc_a) // 100 
        aumento_ano_b = (pop_b * cresc_b) // 100 

        pop_a = pop_a + aumento_ano_a 
        pop_b = pop_b + aumento_ano_b 
        qtd_anos_passaram += 1

    if (qtd_anos_passaram <= 100):
        print("{:d} anos.".format(qtd_anos_passaram))

    else:
        print("Mais de 1 seculo.")