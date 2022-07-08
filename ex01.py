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
        self.login = login

    #getters
    @property
    def nome(self):
        return self._nome

    @property
    def senha(self):
        return self._senha

    @property
    def login(self):
        return self._login

    #setters
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @senha.setter
    def senha(self, valor):
        self._senha = valor

    @login.setter
    def login(self, valor):
      if valor:
        self._login = valor
        print(f'{self.nome} já está logado no sistema')
        return
      else:
        self._login = valor
        print(f'{self.nome} não está logado no sistema')
        return


