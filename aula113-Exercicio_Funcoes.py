#Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
não nomeados recebidos e retorne o total para uma variável. Mostre
o valor da variável no final.
"""

"""
Crie uma função que fala se um número é par ou ímpar.
Retorne se é par ou ímpar.
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplicar(1, 2, 3, 4, 5)
print(resultado)

def par_impar(num):
    if(num % 2 == 0):
        return f"{num} é par!"
    return f"{num} é ímpar!"

numero = par_impar(117)
print(numero)