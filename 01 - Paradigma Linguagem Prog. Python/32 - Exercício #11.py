def éPrimo(p):
    cont = 0
    for i in range(1, p + 1):
        if p % i == 0:
            cont += 1
    if cont == 2:
        return True


n = int(input('Digite um número: '))
primo = éPrimo(n)
if primo == True:
    print(f'\nO número {n} é um número Primo\n')
else:
    print(f'\nO número {n} NÃO é um número Primo\n')