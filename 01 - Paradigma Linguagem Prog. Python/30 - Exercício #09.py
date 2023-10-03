def éPar(n):
    n = (n % 2 == 0)
    return n

def somaPar(list):
    soma = 0
    for i in list:
        if éPar(i):
            soma += i
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = somaPar(lista)
print(f'\nA soma dos números pares da lista {lista} é {soma}\n')