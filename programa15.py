def calcular_idade(ano_nascimento, ano_atual = 2024):
    idade = ano_atual - ano_nascimento
    print(f'Você completou {idade} anos em {ano_atual}.')


# calcular_idade(1985, 2024)
# calcular_idade(1997, 2024)
# calcular_idade(2000, 2024)

calcular_idade(1985)
calcular_idade(1997, 2020)
calcular_idade(2000)
calcular_idade(ano_atual=2024, ano_nascimento=1950)