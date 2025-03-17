'''
Escreva uma função em Python que recebe um número como parâmetro e retorna 
o dobro desse número. Em seguida, escreva um programa que pede ao usuário 
para digitar um número, chama a função para calcular o dobro do número digitado e exibe 
o resultado na tela.
'''
def dobro(num):
    return num * 2

def main():
    numero = input("Digite um número: ")
    numero_int = float(numero)
    dobro_numero = dobro(numero_int)
    print(f"O dobro do número {numero_int} é {dobro_numero}")

#main()

'''
Escreva uma função em Python que recebe uma lista de números como parâmetro e 
retorna a média desses números. Em seguida, escreva um programa que pede ao usuário 
para digitar uma lista de números separados por vírgulas, 
chama a função para calcular a média desses números e exibe o resultado na tela.
A fórmula para calcular a média de uma lista de números é simples: basta somar todos os 
elementos da lista e dividir o resultado pelo número de elementos na lista. Matematicamente, 
a fórmula para calcular a média pode ser escrita da seguinte forma:

Média = (x1 + x2 + ... + xn) / n

Onde:

    x1, x2, ..., xn são os elementos da lista de números.
    n é o número de elementos na lista.
'''
import re

def media_lista(lista):
    total = 0
    for numero in lista:
        numero_int = int(numero)
        total += numero_int
    
    media = total / len(lista)
    return media

def main2():
    numeros = input("Digite uma lista de números separando por vírgula: ").replace(" ", "")
    numeros_limpos = numeros.split(",")
    lista_numeros = list(numeros_limpos)

    print(lista_numeros)

    media_final_lista = media_lista(lista_numeros)
    print(f"A média dos valores na lista é: {media_final_lista:.2f}")

#main2()

"""
Escreva uma função chamada soma_quadrados que recebe dois números 
inteiros como parâmetros e retorna a soma dos seus quadrados. Em seguida
escreva um programa que solicita que o usuário digite dois números inteiros,
chama a função soma_quadrados com esses números e exibe o resultado.

#formula 

a² + b²
onde "a" e "b" são os números que queremos elevar ao quadrado e somar.

#exemplo de saida

Digite um número inteiro: 3
Digite outro número inteiro: 4
A soma dos quadrados de 3 e 4 é 25.

"""
def soma_quadrado(num1, num2):
    return (num1 ** 2) + (num2 ** 2)

def main3():
    numero1 = input("Digite um número inteiro: ")
    numero2 = input("Digite outro número interio: ")
    numero1_int = int(numero1)
    numero2_int = int(numero2)

    resultado_operacao = soma_quadrado(numero1_int, numero2_int)
    print(f"A soma dos quadrados de {numero1_int} e {numero2_int} é {resultado_operacao}")

#main3()

'''
Escreva um programa que recebe uma lista de números
inteiros como entrada e retorna a soma dos elementos da lista.
'''
def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

lista_inteiros = [2, 3, 4, 5, 6, 7]
soma_numeros = soma_lista(lista_inteiros)
print(f"A soma dos inteiros da lista é {soma_numeros}")