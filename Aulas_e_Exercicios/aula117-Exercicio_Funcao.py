"""
Exercício
Crie funções que duplicam, triplicam e quadruplicam o número
recebido como parâmetro.
"""

def criar_multiplicador(valor):
    def realiza_multiplicacao(num):
        return num * valor
    return realiza_multiplicacao

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))