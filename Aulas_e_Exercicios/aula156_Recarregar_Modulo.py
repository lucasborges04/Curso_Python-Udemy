# Recarregando módulos, importlib e singleton
import importlib
 
import aula156_Recarregar_Modulo_m
 
print(aula156_Recarregar_Modulo_m.variavel)
 
for i in range(10):
    importlib.reload(aula156_Recarregar_Modulo_m)
    print(i)
 
print('Fim')