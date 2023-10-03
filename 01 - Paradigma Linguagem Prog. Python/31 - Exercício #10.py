def fat(i):
    if i == 0 or i == 1:
        return i
    return i * fat(i - 1)

n = int(input('\nDigite um número para calcular seu fatorial: '))
fatorial = fat(n) 
print(f'O Fatorial de {n} é {fatorial}\n')