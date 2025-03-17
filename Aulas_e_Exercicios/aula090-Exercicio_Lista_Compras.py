"""
Faça uma lista de compras
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices
inexistentes na lista.
"""
import os

lista_compras = []

while(True):
    print("Selecione uma opção:")
    opcao = input("[i]nserir [a]pagar [l]istar: ").lower()

    if(opcao.startswith("i")):
        inserir_valor = input("Valor: ")
        lista_compras.append(inserir_valor)
        print("Valor adicionado na lista com sucesso!\n")

    elif(opcao.startswith("a")):
        apagar_valor = input("Escolha o índice para apagar o valor: ")
        apagar_valor_int = int(apagar_valor)

        for indice, valor in enumerate(lista_compras):
            if(apagar_valor_int == indice):
                del lista_compras[indice]
                print("Valor apagado da lista com sucesso!\n")

    elif(opcao.startswith("l")):
        os.system("cls")
        if(lista_compras != []):
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
            print()
            
        else:
            print("A lista está vazia!\n")
    else:
        print("Opção inválida! Digite uma opção válida.\n")