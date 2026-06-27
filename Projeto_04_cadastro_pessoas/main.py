# Sistema de Cadastro de Pessoas

print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)

nome = input('Nome: ').strip()
idade = int(input('Idade: '))
cidade = input('Cidade: ').strip()

pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}

print(pessoa['nome'])
