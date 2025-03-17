import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10
resultado_soma_1 = 0

for numero in nove_digitos:
    resultado_soma_1 += int(numero) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_soma_2 = 0

for numero in dez_digitos:
    resultado_soma_2 += int(numero) *contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"

print(cpf_gerado_pelo_calculo)