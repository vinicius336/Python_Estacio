hora = 10
minuto = 26
segundo = 18
print()
print(hora, ':', minuto, ':', segundo)
print(str(hora) + ' : ' + str(minuto) + ' : ' + str(segundo))
print('{} : {} : {}\n' .format(hora, minuto, segundo))
print(f'{hora} : {minuto} : {segundo}')

print('Formatando a largura do campo')
print('.{:4}.:{:3}.:{:2}\n' .format(hora, minuto, segundo))

# Impressão com 8 espaços mas só 5 serão utilizados
print('{:8.5}' .format(10/3))

print('\nImprimindo sequências')
seq = [0, 1, 2]
print(seq)

# Imprimindo Substrings
str = 'Hello World'
print(str[0:5])

# Imprimindo invertido
print('\n',str[::-1])