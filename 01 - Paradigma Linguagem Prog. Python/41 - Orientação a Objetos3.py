class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def imprimir(self):
        print(f'{self.nome} tem {self.idade} ano(s)')
        
    def getIdade(self):
        return self.idade
    
    def setIdade(self):
        return self.idade


class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        print(f'Profissão: {self.profissao}\n')

p = Pessoa('Ana', 25)
p = Profissional('Ana', 25, 'balconista')
print()
p.imprimir()