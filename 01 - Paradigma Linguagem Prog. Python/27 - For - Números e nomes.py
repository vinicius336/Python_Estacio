print()
for i in range(2, 9, 3):
    print(i)

nome = input('\nDigite seu nome: ')
for i in nome:
    print(i)
print()

nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for i in nomes:
    print(i)
print()

for i in range(10):
    if i == 5:
        continue
    else:
        print(i, end=' ')
print()

for i in range(10):
    if i == 5:
        break
    else:
        print(i, end=' ')
print()

for i in range(10):
    if i == 5:
        pass
    else:
        print(i, end=' ')
print()