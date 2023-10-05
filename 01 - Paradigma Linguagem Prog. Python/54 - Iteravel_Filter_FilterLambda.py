#   Função Iterável
lista = [1, 2, 3, 4, 5]
def impar(iteravel):
    lista_aux = []
    for item in iteravel:
        if item % 2 != 0:
            lista_aux.append(item)
    return lista_aux
def main():
    nova_lista = impar(lista)
    print(nova_lista)
if __name__ == '__main__':
    main()
    
#   Função Filter
lista = [1, 2, 3, 4, 5]
def impar(item):
    if item % 2 != 0:
        return item
def main():
    nova_lista = filter(impar, lista)
    print(list(nova_lista))
if __name__ == '__main__':
    main()

#   Função Filter com Lambda
lista = [1, 2, 3, 4, 5]
nova_lista = filter(lambda item: item % 2 != 0, lista )
def main():
    print(list(nova_lista))
if __name__ == '__main__':
    main()