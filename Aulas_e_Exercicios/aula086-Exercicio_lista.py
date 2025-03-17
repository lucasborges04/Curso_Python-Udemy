"""
Exiba os índices da lista
"""
lista = ["Maria", "Helena", "Luiz"]

for i in range(len(lista)):
    print(i)

#Para aparecer os nome na frente de cada índece, poderia fazer:

for i in range(len(lista)):
    print(i, lista[i])