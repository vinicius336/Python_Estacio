from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #   Um método de classe para criar um objeto Pessoa através do ano de nascimento
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    #   Mérodo Estático: verificar se é maior de idade.
    @staticmethod
    def éMaiorIdade(idade):
        return idade >= 18
    
pessoa1 = Pessoa('Maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006)
print()
print(pessoa1.idade)
print(pessoa2.idade)
#   Imprimir o resultado
print(Pessoa.éMaiorIdade(18))
print()