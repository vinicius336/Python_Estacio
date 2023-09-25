print()
x = 10; y = 20
print('10 = {}{}\n' .format(x, type(x)))

print('Operador + | Soma\n10(int) + 10( int ) = {}    {}\n' .format(x + x, type(x + x)))

x = 10.0
print('Operador - | Subtração\n20(int) - 10(float) = {}  {}\n' .format(y - x, type(y - x)))

x = 10,0
print('x = 10,0> > > > > > >{}{}\n' .format(x, type(x)))

print('Operador * | Multiplicação\n2 * 3 = {}\n' .format(2 * 3))

print('Operador ** | Exponenciação\n2  ( int )**3(int) = {}   {}' .format(2**3, type(2**3)))

print('2.0(float)**3(int) = {} {}\n3.0(float)**2(int) = {} {}\n' .format(2.0**3, type(2.0**3), 3.0**2, type(3.0**2)))

print('Operador / | Divisão\n6(int)/2(int) = {} {}' .format(6/2, type(6/2)))

print('5(int)/2(int) = {} {}\n' .format(5/2, type(5/2)))

print('Operador // | Quociente inteiro\n21(int)//2(int) = {} {}\n' .format(21//2, type(21//2)))

print('Operador % | Resto inteiro\n21(int)%2(int) = {} {}\n' .format(21%2, type(21%2)))

r = complex(2, 5)
print('Número complexo\nx+yj = {} {}' .format(r, type(r)))
w = 2 + 5j
print('{} {}\n' .format(w, type(w)))

print('Booleano\n2 > 3 = {}\n2 < 3 = {}\n' .format(2 > 3, 2 < 3))

print('Operador NOT\nNOT(2 > 3) = NOT({}) = True\n' .format(2 > 3))

print('Operador E\n(4 > 3) E (3 > 2) = {}' .format(4 > 3 and 3 > 2))
print('(4 > 3) E (3 < 2) = {}' .format(4 > 3 and 3 < 2))
print('(4 < 3) E (3 > 2) = {}' .format(4 < 3 and 3 > 2))
print('(4 < 3) E (3 < 2) = {}\n' .format(4 < 3 and 3 < 2))

print('Operador OU\n(4 > 3) OU (3 > 2) = {}' .format(4 > 3 or 3 > 2))
print('(4 > 3) OU (3 < 2) = {}' .format(4 > 3 or 3 < 2))
print('(4 < 3) OU (3 > 2) = {}' .format(4 < 3 or 3 > 2))
print('(4 < 3) OU (3 < 2) = {}\n' .format(4 < 3 or 3 < 2))

print('Operador abs | Valor Absoluto\nabs(-2.5) = {}\n' .format(abs(-2.5)))

print('''Operadores de Comparação
<  Menor que      | 2 <  3
<= Menor ou igual | 2 <= 3
>  Maior que      | 3 >  2
>= Maior ou igual | 3 >= 2
== Igual          | 2 =  2
!= Diferente      | 2 != 3
''')
print('OBS: O símbolo de COMPARAÇÃO == é diferente do símbolo de ATRIBUIÇÃO =')

print('''STRINGS
>> São qualquer sequencia de caracteres de qualquer tipo, em uma determinada declaração do tipo str
>> Podem ser escritas pos:
    >> Aspas Simples        - 'string'
    >> Aspas Duplas         - "string"
    >> Aspas Simples triplas- \'\'\'string\'\'\'
    >> Aspas Duplas triplas - """string"""
''')
print('''Métodos de tratamento de Strings
upper()     - Transforma todas as letras em maiúsculas
lower()     - Transforma todas as letras em minúsculas
split()     - Quebra a string em substrings(separação por espaços)
''')

print()