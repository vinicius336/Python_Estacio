from sklearn.datasets import load_digits
digitos = load_digits()

# Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64
print(f'Shape dos dados de imagens: {digitos.data.shape}')

# Apresentar o total de dados rotulados com inteiros de 0 a 9
print(f'Shape dos dados rotulados: {digitos.target.shape}')