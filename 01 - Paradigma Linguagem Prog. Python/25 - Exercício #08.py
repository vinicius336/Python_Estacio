lista = [10, 2, 5, 7, 6, 3]
soma = 0
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        soma += lista[i]
print('A soma dos números pares da lista é: {}' .format(soma))