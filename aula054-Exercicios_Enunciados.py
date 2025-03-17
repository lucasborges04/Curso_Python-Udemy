"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input("Digite um número: ")

try:
    numero_int = int(numero_str)
    if(numero_int % 2 == 0):
        print(f"{numero_int} é par.")
    else:
        print(f"{numero_int} é primo.")
except:
    print("Erro: você deve digitar um número inteiro.")

"""
Como foi resolvido no curso:

entrada = input("Digite um número: ")

if entrada.isdigit(): #Verifica se o valor inserido é um número
    entrada_int = int(entrada) #Converte para um número inteiro
    par_impar = entrada_int % 2 == 0 #Se for par retorna True, se não False
    par_impar_texto = 'ímpar' 

    if par_impar: #Se for par (True)
      par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input("Informe a hora em inteiro (Ex: 2): ")

try:
    hora_int = int(hora_str)

    if(0 <= hora_int <= 11):
        print("Bom dia!")
    elif(hora_int <= 17):
        print("Boa tarde!")
    elif(hora_int <= 23):
        print("Boa noite!")
    else:
        print("Erro: O dia só tem 24 horas (máximo 23h)!")

except:
    print("Erro: Você deve digitar um número inteiro!")

#OBS: Poderia ser feito usando o isdigt() assim como na questão anterior.

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input("Digite seu nome: ")

if(len(primeiro_nome)<= 4):
    print("Seu nome é curto!")
elif(len(primeiro_nome) <= 6):
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")

"""
Como foi resolvido no curso:

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1: #Verifica se o nome tem mais de uma letra
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
"""