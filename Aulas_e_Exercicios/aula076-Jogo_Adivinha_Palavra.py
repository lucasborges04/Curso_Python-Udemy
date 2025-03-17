"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secret qualquer e vai dar a
possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se 
a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada nõ estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

while(True):
    palavra_secreta = "batata"
    palavra_secreta_formatada = "******"
    cont = 0 #Conta as tentativas feita pelo usuário

    while(True):
        inserir_letra = input("Digite uma letra: ")
        palavra = ""

        if(len(inserir_letra) > 1):
            cont += 1
            print("Digite apenas uma letra.")
            continue

        for i in range(len(palavra_secreta)):
            if(palavra_secreta[i] == inserir_letra): #Se a letra estiver no indice i da palavra_secreta
                palavra += inserir_letra #Adicionamos a letra na variavel palavra
            else:
                palavra += palavra_secreta_formatada[i] #Se não, adicionamos o asterisco
            
        palavra_secreta_formatada = palavra #Atualiza a palavra_secreta_formatada
        print(f"Palavra: {palavra_secreta_formatada}") #Mostra como ficou a palavra após a tentativa
        cont += 1

        if("*" not in palavra_secreta_formatada):
            print("PARABÉNS! Você acertou a palavra.")
            print(f"Tentativas: {cont}")
            print(f"A palavra era: {palavra_secreta}")
            break