#
#
# 1. Exercício 1:
# – Crie a classe Usuario com os atributos nome, login e senha.
# – Como você implementaria a classe para que o atributo nome só salvasse nomes
# com CAIXA ALTA e senha uma String?
# – Implemente!!!

class Usuario:
    def __init__(self, nome,  senha: str, login = False): # login = False é o valor padrão do atributo login se não
                                                           # for passado nada na chamada do método
        self.nome = nome.upper() # O atributo nome só salva nomes com caixa alta
        self.senha = senha # O atributo senha é uma String
        self.login = login # O atributo login é um boolean que indica se o usuário está logado ou não

    #getters
    @property
    def nome(self):
        return self._nome

    @property # O atributo senha é uma String
    def senha(self):
        return self._senha

    @property
    def login(self): # O atributo login é um boolean que indica se o usuário está logado ou não
        return self._login

    #setters
    @nome.setter
    def nome(self, valor): # O atributo nome só salva nomes com caixa alta
        self._nome = valor.upper()

    @senha.setter
    def senha(self, valor: str): # O atributo senha é uma String
        self._senha = valor

    @login.setter
    def login(self, valor: bool): # O atributo login é um boolean que indica se o usuário está logado ou não
      if valor:
        self._login = valor
        print(f'{self.nome} já está logado no sistema')
        return
      else:
        self._login = valor
        print(f'{self.nome} não está logado no sistema')
        return


