# Atribuição Múltipla
a, b = 1, 2
print('\nAntes da troca')
print(f'Valor das variáveis a = {a} e b = {b}')
#Primeira troca
temp = a
a = b
b = temp
print('Primeira troca')
print('O valor das variáveis a = {} e b = {}' .format(a, b))
#Segunda troca
a, b = b, a
print('Segunda troca')
print('O valor das variáveis a = {} e b = {}\n' .format(a, b))