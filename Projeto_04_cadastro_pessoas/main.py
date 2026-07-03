# Sistema de Cadastro de Pessoas

print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)

pessoas = []

continuar = True

while continuar:
    print('''1 - Adicionar Pessoa
2 - Listar Pessoa
3 - Sair''')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        pessoa = {}
        while True:
            nome = input('Nome: ').strip()
            if nome == '':
                print('ERRO! O nome não pode estar vazio.')
            else:
                pessoa['Nome'] = nome
                break

        while True:
            try:
                pessoa['Idade'] = int(input('Idade: '))
                break
            except:
                print('ERRO! Digite apenas números.')
        
        while True:
            cidade = input('Cidade: ').strip()
            if cidade  == '':
                print('ERRO! A cidade não pode estar vazia')
            else:
                pessoa['Cidade'] = cidade
                break
        pessoas.append(pessoa)
        print('\nPessoa cadastrada com sucesso.')    

    elif opcao == '2':
        if not pessoas:
            print('Nenhuma cadastro foi realizado.')
        else: 
            print('='*20)           
            print('PESSOAS CADASTRADAS')
            print('='*20)
            print(f'Total de pessoas cadastradas: {len(pessoas)}')
            print()
            for i, pessoa in enumerate(pessoas):
                print(f'===== PESSOA {i + 1} =====')
                for campo, dado in pessoa.items():
                    print(f'{campo}: {dado}')
                print()

    elif opcao == '3':
        continuar = False
