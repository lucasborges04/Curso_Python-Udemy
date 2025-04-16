from sys import path
# from sys import path

import aula158_package.modulo
from aula158_package import modulo
from aula158_package.modulo import *
# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo
# # from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula158_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
from aula158_package.modulo import fala_oi, soma_do_modulo

print(__name__)
fala_oi()