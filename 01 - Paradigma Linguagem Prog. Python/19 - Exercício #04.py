peso = eval(input('\nDigite o peso em Kg: '))
altura = eval(input('Digite a altura em cm: '))
IMC = peso / (altura / 100) ** 2
print('{:.2f}\n' .format(IMC))