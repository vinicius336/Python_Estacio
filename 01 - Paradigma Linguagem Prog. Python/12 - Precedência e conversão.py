print('\nOrdem de precedência de operações\n')
print('Abaixo é listada a precedência de operadores. Operadores na mesma linha tem precedência da esquerda para a direita.')
print('''
    [expressões ...]                -   Definição de lista
    x[], x[índice: índice]          -   Operador de indexação
    **                              -   Exponenciação
    +x, -x                          -   Sinal positivo e negativo
    *, /, //, %                     -   Produto, divisão, divisão inteira, resto
    +, -                            -   Soma, subtração
in, not in, <, <=, >, >=, !=, ==    -   Comparações, inclusive em listas
    not x                           -   Booleano not (NÃO)
    and                             -   Booleano and (E)
    or                              -   Booleano or (OU)
''')
print('Valores Inteiros e Reais podem ser convertidos como no exemplo abaixo:\n')
print('2(int) + 2(float) = {}' .format(2 + 2.0))
print('\nDa mesma forma podemos converter um booleano:\n{} + 2 = {}\n{} + 1 = {}\n' .format(True, True + 2, False, False + 1))

print('Conversões Explícitas\nSe x = 2   então float(2) = {}\nLogo:.\nSe x = 5.1 então int(5.1) = {}\n' .format(float(2), int(5)))