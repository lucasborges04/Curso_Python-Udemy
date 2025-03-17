#Não é muito prudente usar dessa maneira o Try/Except
#Mais para frente do curso, será relatado a maneira mais correta.
numero_str = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero_str)
    print("Float:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:
    print("Isso não é um número.")