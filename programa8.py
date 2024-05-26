ec2_ligado = True
rds_ligado = False

print (f'A instância ec2 está ligada? {ec2_ligado}')
print (f'O banco de dados está ligado? {rds_ligado}')

print(not True)
print(not False)

# Operadores Lógicos (AND, OR & NOT)

# x y AND
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

# x y OR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

print(ec2_ligado and rds_ligado)

# Operadores Relacionais

idade = 30
maior_de_idade = idade >= 18
profissao = 'Dev'

objetivo_cumprido = idade >= 30 and profissao == 'Dev'

print(f"É maior de idade? {maior_de_idade}")
print(f"Objetivo cumprido? {maior_de_idade}")