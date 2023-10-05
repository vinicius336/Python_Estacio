class Veiculo:
    def __init__(self, nome, v_max, km_L):
        self.nome = nome
        self.v_max = v_max
        self.km_L = km_L

    def imprimir(self):
        print(f'Marca: {self.nome}\nVelocidade: {self.v_max}\nKM / L: {self.km_L}')

class Onibus(Veiculo):      #Classe filha que herda as variáveis e métodos da classe Veículo
    pass

print()
onibus = Veiculo('Mercedes', 100, 1000)
carro1 = Veiculo('VolksWagen Fusca', 180, 10)
carro2 = Veiculo('VolksWagen Up', 220, 22)
onibus.imprimir();  print()
carro1.imprimir();     print()
carro2.imprimir();     print()