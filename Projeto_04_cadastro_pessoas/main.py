# Sistema de Cadastro de Pessoas

print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)
pessoa = {}

pessoa['Nome'] = input('Nome: ').strip()
pessoa['Idade'] = int(input('Idade: '))
pessoa['Cidade'] = input('Cidade: ').strip()

print('\n=== DADOS CADASTRADOS ===')

for campo, dado in pessoa.items():
    print(f'{campo}: {dado}')
