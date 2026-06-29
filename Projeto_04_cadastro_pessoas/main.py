# Sistema de Cadastro de Pessoas

print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)
pessoa = {}

while True:
    nome = input('Nome: ').strip()
    if nome == '':
        print('ERRO! O nome não pode estar vazio.')
    else:
        pessoa['Nome'] = nome
        break

pessoa['Idade'] = int(input('Idade: '))

while True:
    cidade = input('Cidade: ').strip()
    if cidade  == '':
        print('ERRO! A cidade não pode estar vazia')
    else:
        pessoa['Cidade'] = cidade
        break

print('\n=== DADOS CADASTRADOS ===')

for campo, dado in pessoa.items():
    print(f'{campo}: {dado}')
