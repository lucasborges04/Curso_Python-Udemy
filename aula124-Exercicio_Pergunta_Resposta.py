# Exercício - sistema de perguntas e respostas
#Resolução da maneira que criei

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

print("-" * 10)
print("\nJogo de Pergunta e Resposta")
acertos = 0

for dicionario in perguntas:
    print()
    for chave, valor in dicionario.items():
        if(chave == "Resposta"):
            resposta_pergunta = int(valor)
            continue
        else:
            print(f"{chave}: {valor}")

    resposta_usuario = input("Qual a resposta? ")
    resposta_usuario_convertida = int(resposta_usuario)

    if(resposta_usuario_convertida == resposta_pergunta):
        print(f"PARABÉNS!!! Você acertou essa questão.")
        acertos += 1
    else:
        print(f"Você errou! A resposta era {resposta_pergunta}")

print(f"\n{acertos}/{len(perguntas)} acertos.")
