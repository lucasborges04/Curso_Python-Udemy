while True:
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    num1_float = float(numero1)
    num2_float = float(numero2)
    operador = input("Digite o operador que deseja fazer a conta(+, -, *, /): ")

    if(operador == "+"):
        resultado = num1_float + num2_float
        print(f"{num1_float} + {num2_float} = {resultado}")
    elif(operador == "-"):
        resultado = num1_float - num2_float
        print(f"{num1_float} - {num2_float} = {resultado}")
    elif(operador == "*"):
        resultado = num1_float * num2_float
        print(f"{num1_float} * {num2_float} = {resultado}")
    elif(operador == "/"):
        resultado = num1_float / num2_float
        print(f"{num1_float} / {num2_float} = {resultado}")
    else:
        print("Opção inválida! Adigite apenas um dos operadores citados.")
    
    sair_calculadora = input("Quer sair do programa(sim / não): ").lower()
    if(sair_calculadora == "sim"):
        break