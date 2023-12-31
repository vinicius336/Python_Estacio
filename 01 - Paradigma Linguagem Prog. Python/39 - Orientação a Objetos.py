class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
        
    def set_nome(self, nome):
        self.nome = nome
        
    def set_ender(self, ender):
        self.ender = ender
        
    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender
    
pessoa1 = Pessoa('Maria', 'Rua C. J. G. de S. F.')
pessoa2 = Pessoa('Sarah', 'Rua N. P.')
print(f'\nNome: {pessoa1.get_nome()}\nEndereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}\nEndereço: {pessoa2.get_ender()}\n')