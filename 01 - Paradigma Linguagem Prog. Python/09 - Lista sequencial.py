lista = [101, 202, 303, 404, 505]
print('\nlista[0] = {}' .format(lista[0]))
print('lista[1] = {}' .format(lista[1]))
print('lista[2] = {}' .format(lista[2]))
print('lista[3] = {}' .format(lista[3]))
print('lista[4] = {}' .format(lista[4]))
print('lista = {}' .format(lista))
for i in range(0, 4+1):
    print('lista[{}] = {}\n' .format(i, lista[i])) if i == 5 else print('lista[{}] = {}' .format(i, lista[i]))
print()