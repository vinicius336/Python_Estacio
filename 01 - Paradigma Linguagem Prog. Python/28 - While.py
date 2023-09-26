palavra = input('\nDigite uma palavra: ').upper().strip()
while palavra != 'SAIR':
    print('Você digitou ({})\nPara sair digite [sair]\n' .format(palavra))
    palavra = input('Digite uma palavra: ').upper().strip()
print('({}). Agora você está fora do laço\n' .format(palavra))

print('Laço infinito!\nwhile True:\n    Bloco a ser repetido\n')

while True:
    print('Primeiro Laço!')
    palavra = input('Digite uma palavra: ').upper().strip()
    if palavra == 'SAIR':
        break
    else:
        while True:
            print('Segundo Laço!')
            palavra = input('Sair? [SIM] [NÃO]').upper().strip()
            if palavra == 'SIM':
                break
    print('Fora do segundo Laço!')
print('Fora do primeiro Laço!\n')