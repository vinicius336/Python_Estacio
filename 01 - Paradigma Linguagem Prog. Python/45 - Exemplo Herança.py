class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def somar(self):
        return self.a + self.b
    def multiplica(self):
        return self.a * self.b
    
class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b
    def dividir(self):
        return self.a / self.b
    
x = int(input('\nDigite um número: '))
y = int(input('Digite outro número: '))
d = Derivada(x, y)
print()
print(f'A soma de {d.a} e {d.b} é: {d.somar()}')
print(issubclass(Derivada, ClasseSomaMultiplica))
print()