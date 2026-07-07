# Sistema de Cadastro de Pessoas

print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)

pessoas = []

continuar = True

while continuar:
    print('''1 - Adicionar Pessoa
2 - Listar Pessoa
3 - Buscar Pessoa   
4 - Remover Pessoa       
5 - Sair''')

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
        nome_busca = input('Digite o nome da pessoa: ').strip()
        encontrou = False
        for pessoa in pessoas:
            if nome_busca == pessoa['Nome']:
                encontrou = True
                for campo, dado in pessoa.items():
                    print(f'{campo}: {dado}')
        if not encontrou:
            print('Pessoa não encontrada')   

    elif opcao == '4':
        nome_remover = input('Qual pessoa deseja remover da lista: ').strip()
        encontrou = False
        for pessoa in pessoas:
            if nome_remover == pessoa['Nome']:
                pessoas.remove(pessoa)
                encontrou = True
                print('Pessoa removida com sucesso.')
                break
        if not encontrou:
            print('Pessoa não encontrada')

    elif opcao == '5':
        while True:
            resposta = input('Deseja Realmente Sair? [S/N] ').strip().upper()
            if resposta == '':
                print('Digite S ou N.')
            else:
                resposta = resposta[0]
                if resposta == 'S':
                    print('Saindo...')
                    continuar = False
                    break

                elif resposta =='N':
                    print('Operação cancelada.')
                    break
print('Sistema Finalizado')
