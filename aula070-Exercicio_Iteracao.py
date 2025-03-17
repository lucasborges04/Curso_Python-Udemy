frase = "O Python é uma linguagem de programação multiparadigma. O Python foi criado por Guido Van Rossum.".replace(" ","").lower()

verif_letras = 0 #Variável que faz a contagem para percorrer letra por letra(utilizada no primeiro loop)
maior_freq = 0 #Variável para armazenar a quantidades de vezes que determinada letra apareceu
letra_maior_freq = frase[0] #Variável para armazenar a letra com maior frequencia na frase

while(verif_letras < len(frase)):
    freq_letra = 0 #Variável para armazenar o tanto de vezes que a letra apareceu na frase
    letra = frase[verif_letras] #Pega a primeira letra para verificar com as demais
    cont = 0 #variavel que percorre letra por letra no segundo loop para fazer a verificação

    while(cont < len(frase)):
        
        if(letra == frase[cont]):
            freq_letra += 1

        cont += 1

    if(freq_letra > maior_freq):
        maior_freq = freq_letra
        letra_maior_freq = letra
    
    verif_letras += 1

print(f"A letra que apareceu mais vezes foi '{letra_maior_freq}' com um total de {maior_freq}x.")