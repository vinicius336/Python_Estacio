#   Função Iterável
lista = [1, 2, 3, 4, 5]
def triplica_lista(iteravel):
    lista_aux = []
    for item in iteravel:
        lista_aux.append(item * 2)
    return lista_aux
def main():
    nova_lista = triplica_lista(lista)
    print(nova_lista)
if __name__ == '__main__':
    main()
    
#   Função Map
lista = [1, 2, 3, 4, 5]
def triplica(item):
    return item * 3
def main():
    nova_lista = map(triplica, lista)
    print(list(nova_lista))
if __name__ == '__main__':
    main()

#   Função Map com Lambda
lista = [1, 2, 3, 4, 5]
nova_lista = map(lambda item: item * 4, lista)
def main():
    print(list(nova_lista))
if __name__ == '__main__':
    main()