lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

par = lambda x: x % 2 == 0

pares = list(filter(par, lista))

print(f'\nOs números pares da lista são: {pares}\n')