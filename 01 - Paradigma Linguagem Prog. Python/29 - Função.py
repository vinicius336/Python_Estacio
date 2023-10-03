'''
    Escreva um programa que encontre o menor número de uma lista através de uma função e ao final informe qual é o menor número na tela
    
    - Uma função deve ser declarada e escrita no início do programa, ou antes de ser feita a sua chamada, caso contrário ela não funcionará
    - A palavra reservada 'def' serve para declarar que aquele bloco será a declaração da função
'''

def encontrarMenor(list):
    menor = list[0]
    for i in list:
        if i < menor:
            menor = i
    return menor

lista = [2, 10, 3, 1, 4, 5]
menor = encontrarMenor(lista)
print(f'\nO menor valor da lista é {menor}\n')