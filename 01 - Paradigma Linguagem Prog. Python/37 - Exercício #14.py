exeção = False
while exeção == False:
    try:
        x = int(input('\nDigite um número: '))
        exeção = True
    except:
        print('Entre com um número válido.')
        exeção = False
print(f'Você digitou {x}\n')