Numerador1, Denominador1, Numerador2, Denominador2 = map(int, input().split())

def mdc(Denominador1, Denominador2):
    if (Denominador2 == 0):
        return Denominador1
    return mdc(Denominador2, Denominador1 % Denominador2)

def mmc(Denominador1, Denominador2):
    return abs(Denominador1 * Denominador2) / mdc(Denominador1, Denominador2)

Res_mmc = mmc(Denominador1, Denominador2)
Numerador_final = ((Res_mmc / Denominador1) * Numerador1) + ((Res_mmc / Denominador2) * Numerador2)
Res_mdc = mdc(Res_mmc, Numerador_final)

Fracao_Final_1 = int(Numerador_final / Res_mdc)
Fracao_Final_2 = int(Res_mmc / Res_mdc)

print(Fracao_Final_1, Fracao_Final_2)