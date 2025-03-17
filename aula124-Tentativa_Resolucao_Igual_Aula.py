#Tentativa de resolver o exercício no mesmo formato do exercício passado
#passado no curso

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0

for dicionario in perguntas:
    for chave, valor in dicionario.items():

        if(chave == "Pergunta"):
            print(f"\n{chave}: {valor}")
        else:
            continue
        
        for indice, alternativa in enumerate(dicionario["Opcoes"]):
            print(f"{indice}) {alternativa}")
        
        montar_numero = ''

        for resp in dicionario["Resposta"]:
            montar_numero += resp
        
        resposta_questao = int(montar_numero)
        resposta_usuario = input("Escolha uma opção (0, 1, 2 ou 3): ")
        resposta_usuario_int = int(resposta_usuario)
        acertou = False

        for indice_verificador, verifica_alternativa in enumerate(dicionario["Opcoes"]):
            if(indice_verificador == resposta_usuario_int and int(verifica_alternativa) == resposta_questao):
                print(f"Você acertou!!!")
                acertos += 1
                acertou = True
                break
        
        if(not acertou):
            print("Errou!")

print(f"\nVocê acertou {acertos} de {len(perguntas)} perguntas!")