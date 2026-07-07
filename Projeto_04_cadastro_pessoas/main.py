# Sistema de Cadastro de Pessoas
print('=' * 25)
print('CADASTRO DE PESSOAS')
print('=' * 25)

# Lista que armazena os cadastros
pessoas = []

# Controla a execução do programa
continuar = True

# Loop principal do sistema
while continuar:
    print('''1 - Adicionar Pessoa
2 - Listar Pessoa
3 - Buscar Pessoa   
4 - Remover Pessoa
5 - Editar Pessoa    
6 - Sair''')

    opcao = input('Escolha uma opção: ')
    # Adiciona uma nova pessoa
    if opcao == '1':
        pessoa = {}
        # Validação do nome
        while True:
            nome = input('Nome: ').strip()
            if nome == '':
                print('ERRO! O nome não pode estar vazio.')
            else:
                pessoa['Nome'] = nome
                break
        # Validação da idade
        while True:
            try:
                pessoa['Idade'] = int(input('Idade: '))
                break
            except:
                print('ERRO! Digite apenas números.')
        # Validação da cidade
        while True:
            cidade = input('Cidade: ').strip()
            if cidade == '':
                print('ERRO! A cidade não pode estar vazia')
            else:
                pessoa['Cidade'] = cidade
                break
        pessoas.append(pessoa)
        print('\nPessoa cadastrada com sucesso.')    
    # Lista todas as pessoas cadastradas
    elif opcao == '2':
        if not pessoas:
            print('Nenhuma pessoa foi cadastrada.')
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
    # Busca uma pessoa pelo nome
    elif opcao == '3':
        nome_busca = input('Digite o nome da pessoa: ').strip()
        encontrou = False
        for pessoa in pessoas:
            if nome_busca == pessoa['Nome']:
                encontrou = True
                for campo, dado in pessoa.items():
                    print(f'{campo}: {dado}')
                break
        if not encontrou:
            print('Pessoa não encontrada.')   
    # Remove uma pessoa cadastrada
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
            print('Pessoa não encontrada.')
    # Edita os dados de uma pessoa
    elif opcao == '5':
        nome_editar = input('Qual pessoa deseja editar: ').strip()
        encontrou = False
        for pessoa in pessoas:
            if nome_editar == pessoa['Nome']:
                encontrou = True
                print('\n1 - Nome')
                print('2 - Idade')
                print('3 - Cidade')

                editar = input('O que deseja editar: ')
                if editar == '1':
                    while True:
                        nome = input('Nome: ').strip()
                        if nome == '':
                            print('ERRO! O nome não pode estar vazio.')
                        else:
                            pessoa['Nome'] = nome
                            print('Cadastro atualizado com sucesso.')                 
                            break
                    break
                
                elif editar == '2':
                    while True:
                        try:
                            pessoa['Idade'] = int(input('Idade: '))
                            print('Cadastro atualizado com sucesso.') 
                            break
                        except:
                            print('ERRO! Digite apenas números.')
                    break
                
                elif editar == '3':
                    while True:
                        cidade = input('Cidade: ').strip()
                        if cidade == '':
                            print('ERRO! A cidade não pode estar vazia')
                        else:
                            pessoa['Cidade'] = cidade
                            print('Cadastro atualizado com sucesso.')
                            break
                    break
                else:
                    print('Opção Inválida.')
                    break
    # Encerra o programa                 
    elif opcao == '6':
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

                elif resposta == 'N':
                    print('Operação cancelada.')
                    break
    else:
        print('Opção inválida.')

print('Sistema finalizado')
