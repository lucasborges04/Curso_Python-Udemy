# Exerício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#Caso queira usar o valor da lista maior, usar o módulo itertools
from itertools import zip_longest

def zipper(lista1, lista2):
    intervalo = min(len(l1), len(l2))
    return [(lista1[i], lista2[i]) for i in range(intervalo)]
    

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))
print(list(zip(l1, l2))) #Função que serve para fazer a mesma coisa do script a cima
print(list(zip_longest(l1, l2, fillvalue='Sem Cidade')))