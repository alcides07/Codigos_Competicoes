Codigo, N_Pecas, Valor_Unitario = map(float, input().split())
Codigo2, N_Pecas2, Valor_Unitario2 = map(float, input().split())

Valor_1 = N_Pecas * Valor_Unitario
Valor_2 = N_Pecas2 * Valor_Unitario2

print("VALOR A PAGAR: R$","{:.2f}".format(Valor_1 + Valor_2))