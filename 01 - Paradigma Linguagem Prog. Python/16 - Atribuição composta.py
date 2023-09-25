x = 10
a = b = c = d = e = 10
print('\nOperadores de Atribuição Composta:\n')
print('\nSendo x = 10\n')
print('x = x + 1 EQUIVALE A x += 1\n')

a = a + 1
print('a = a + 1 >> {}' .format(a))
a += 1
print('a += 1    >> {}\n' .format(a))

b = b - 1
print('b = b - 1 >> {}' .format(b))
b -= 1
print('b -= 1    >> {}\n' .format(b))

c = c * 2
print('c = c * 2 >> {}' .format(c))
c *= 2
print('c *= 2    >> {}\n' .format(c))

d = d / 2
print('d = d / 2 >> {}' .format(d))
d /= 2
print('d /= 2    >> {}\n' .format(d))

e = e ** 3
print('e = e ** 3 >> {}' .format(e))
e **= 3
print('e **= 3    >> {}\n' .format(e))
