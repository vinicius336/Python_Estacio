exeção = True
while exeção == True:
    try:
        x = int(input('\nDigite um número: '))
        exeção = True
    except:
        print('Entre com um número válido.\n')
        exeção = False