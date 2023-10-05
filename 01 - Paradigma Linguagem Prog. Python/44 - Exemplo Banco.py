class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerarExtrato(self):
        print(f'\nNome do Titular: {self.nomeTitular}\nCPF: {self.cpf}\nNúmero: {self.numero}\nSaldo: {self.saldo}\n')
    
def main():
    c1 = Conta(1, 1, 'Vinícius', 0)         #   Valores iniciais da conta
    c1.depositar(300)                       #   Valor depositado na conta
    saque = c1.sacar(300)                   #   Valor a ser sacado
    c1.gerarExtrato()                       #   Mostra na tela informações do extrato
    print(f'O saque foi realizado? {saque}')#   Informa, com base no saldo, se o saque foi realizado
    
if __name__ == '__main__':
    main()