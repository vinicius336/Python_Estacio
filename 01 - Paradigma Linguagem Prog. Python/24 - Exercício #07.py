precoUnitario = 10.00
quantidade = int(input('\nQuantidade comprada: '))
if quantidade <= 10:
    print('\nNão tem desconto.\nO Total a ser pago é: R${}\n' .format(precoUnitario * quantidade))
elif quantidade <= 20:
    print('\nDesconto de 10%\nO Total a ser pago é: R${}\n' .format(precoUnitario * quantidade * .9))
else:
    print('\nDesconto de 20%\nO Total a ser pago é: R${}\n' .format(precoUnitario * quantidade * .8))