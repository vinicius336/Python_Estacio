x = int(input('\nDigite o valor de x: '))
y = int(input('Digite o valor de y: '))
try:
    print(f'O resultado da divisão é: {x / y}\n')
except:
    print('O valor de y não pode ser 0.\n')