"""
Higher order functions
Funções de primeira classe
 
Armazenamento em variáveis: funções podem 
ser atribuídas a variáveis como qualquer 
outro objeto em Python.
"""
# exemplo:
 
 
def funcao(x, y):
    return x * y
 
 
mult = funcao # Atribuimos a função 'funcao' à variável 'mult'
print(mult(3, 6)) # Equivalente a funcao(3, 6), retorna 18
print(mult(4, 5)) # Equivalente a funcao(4, 5), retorna 20
 
"""
Passagem como argumentos: funções podem
ser passadas como argumentos para outras
funções. Isso é útil para criar funções
de ordem superior, que são funções que
operam em outras funções.
"""
# exemplo:
 
 
def func(soma, a, b):
    return soma(a, b) #Executa a função soma passando os argumentos 'a' e 'b'
#Nesse caso executa a função 'argumento', pois foi a função passada argumento no print.
 
 
def argumento(a, b):
    return a + b
 
 
print(func(argumento, 3, 5)) #A função 'argumento' é passada como argumento para a função 'func'.
 
"""
Retorno de funções: funções podem retornar
outras funções. Isso é útil para criar funções
geradoras ou para criar funções que geram
outras funções com base em parâmetros.
"""
# exemplo:
 
 
def cria_multiplo(fator):
    def multiplo(x):
        return x * fator
    return multiplo
 
 
dobro = cria_multiplo(2)
triplo = cria_multiplo(3)
 
print(dobro(3))
print(triplo(3))