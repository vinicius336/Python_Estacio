def somar(x, y, z = 50):    #   Caso a variável z não seja passada na chamada da função ela será inicializada com o valor 50
    return x + y + z

print()
print(somar(20, 30))
print(somar(20, 30, 100), '\n')