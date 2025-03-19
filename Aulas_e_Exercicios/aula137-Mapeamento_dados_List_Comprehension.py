# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

#A list comprehension abaixo fica mias fácil de ler, indo de baixo para cima.
novos_produtos = [ #Está dividido as linhas para ficar mais fácil de visualizar (Poderia fazer em 1 linha)
    {**produto, 'preco': produto['preco'] * 1.05} #Pega o preço e aumenta 5% caso seja maior que 20
    if produto['preco'] > 20 else {**produto} #Se o preço for menor que vinte, retorna o produto sem alteração.
    for produto in produtos #Pega cada produto da lista
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')