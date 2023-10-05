veiculos = ['avião', 'carro', 'navio', 'ônibus']

f_maiuscula = lambda x: str.upper(x)

nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(f'\nNomes maiúsculos = {nomes_maiusculos}\n')