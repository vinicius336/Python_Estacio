def entradaDados():
    coeficiente = quantidade = eval(input('Difite o valor do coeficiante: '))
    return coeficiente

def calulaDelta(a, b, c):
    delta = b * b - 4 * a * c
    return delta

import numpy as np
def calculaRaiz(a, b, c, delta):
    if delta < 0:
        resultado = '\nA equação não possui raízes reais\n'
    elif delta == 0:
        x = -b / (2*a)
        resultado = f'\nA equação possui apenas a raíz {x}\n'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        resultado = f'\nA equação possui as raízes: {x1:2} e {x2:2}'
    return resultado

#f(x) = ax^2 + bx + c
a = entradaDados()
b = entradaDados()
c = entradaDados()
delta = calulaDelta(a, b, c)
resultado = calculaRaiz(a, b, c, delta)
print(f'{resultado}')