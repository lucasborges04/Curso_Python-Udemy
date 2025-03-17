"""
Iterando strings com while
"""
nome = "Lucas"

cont = 0
tamanho_nome = len(nome)
nome_modificado = ""

while(cont < tamanho_nome):
    letra = nome[cont]
    nome_modificado += f"*{letra}"
    cont += 1

nome_modificado += "*"
print(nome_modificado)