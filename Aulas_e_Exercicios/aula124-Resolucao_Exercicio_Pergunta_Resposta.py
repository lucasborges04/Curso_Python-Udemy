#Resolução do exercício (Igual da aula/como o professor fez):

# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for dicionario in perguntas: #Pega cada dicionario da lista 'perguntas'
    print('Pergunta:', dicionario['Pergunta'])
    print()

    opcoes = dicionario['Opções']
    for indice, opcao in enumerate(opcoes): #Imprime cada opção com seu índice atrás dos valores
        print(f'{indice})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit(): #Verifica se é um número inteiro (apenas digitos)
        escolha_int = int(escolha)
    else:
        print("Opção inválida! Digite um número inteiro.")

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == dicionario['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')