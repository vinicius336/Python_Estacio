idade = int(input('\nInforme a idade: '))
if idade < 5:
    print('A criança deve ser vacinada contra a gripe.\nProcure um posto de saúde.\n')
elif idade == 5:
    print('A vacina estará disponível em breve.\nAguarde mais informações.\n')
else:
    print('A vacinação só ocorrerá nos próximos 3 meses.\nInforme-se novamente neste prazo.\n')
print('Vacinas Salvam!\n')