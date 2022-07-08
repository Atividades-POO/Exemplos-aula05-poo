#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 07/07/2022
#
# importando a class Usuario do arquivo ex01.py
from ex01 import Usuario # importando a class Usuario do arquivo ex01.py

# instanciando a classe Usuario
u1 = Usuario('Davi', '123456')
print(f'Nome: {u1.nome}')
print("logando no sistema...")
u1.login = True
print("_________________________________________________")

print("saindo do sistema...")
u1.login = False


