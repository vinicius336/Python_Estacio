def soma(a, b):
    return a + b
def subtrai(a, b):
    return a - b
def multiplica(a, b):
    return a * b
def divide(a, b):
    return a / b

x = int(input('\nDigite um número: '))
y = int(input('Digite um número: '))

print(f'\nA soma de {x} e {y} é {soma(x, y)}')
print(f'A subtração de {x} e {y} é {subtrai(x, y)}')
print(f'A multiplicação de {x} e {y} é {multiplica(x, y)}')
print(f'A divisão de {x} e {y} é {divide(x, y)}\n')
print(f'A soma com a função lambda é: {(lambda a,b: a + b)(x, y)}')
print(f'a subitração com a função lambda é: {(lambda a,b: a - b)(x, y)}')
print(f'a multiplicação com a função lambda é: {(lambda a,b: a * b)(x, y)}')
print(f'a divisão com a função lambda é: {(lambda a,b: a / b)(x, y)}\n')