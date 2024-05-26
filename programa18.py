datas = [3, 14, 9, 22, 8]
animais = ["gato", "cachorro", "coelho", "baleira","porco"]
dados = {
    'nome': 'Luke',
    'email': 'luke@gmail.com',
    'nascimento': 1997
}


for animal in animais:
    print(f'Eu tenho um {animal}.')

for chave in dados:
    print(f'O valor do {chave} é {dados[chave]}')

for numero in range(10, 21):
    print(numero)

print('-----')
print(datas)

for indice, data in enumerate(datas):
    datas[0] = data * 2
    print(f'Indice {indice} data {datas[indice]}')

print(datas)