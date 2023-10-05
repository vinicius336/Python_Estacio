class Veiculo:
    def __init__(self, nome, v_max, km_L):
        self.nome = nome
        self.v_max = v_max
        self.km_L = km_L
    
    def toStr(self):
        print(f'Modelo = {self.nome}\nVelocidade Máxima: {self.v_max}\nQuilometros / Litro: {self.km_L}')
        
modelo_carro1 = Veiculo('VolksWagen Fusca', 180, 10)
modelo_carro2 = Veiculo('VolksWagen Up', 220, 22)
print()
modelo_carro1.toStr()
print()
modelo_carro2.toStr()
print()
