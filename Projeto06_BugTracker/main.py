from json_utils import carregar_bugs, salvar_bugs

# Cadastra um novo bug, adiciona à lista e salva no JSON.
def cadastrar_bug(bugs):
        bug = {}
        # Solicita o nome do bug até que um valor válido seja informado.
        while True:
            titulo_bug = input('Título do bug: ').strip()
            if titulo_bug == '':
                print('ERRO! O título do bug não pode estar vazio.')
            else:
                bug['titulo'] = titulo_bug
                break
        # Solicita a descrição até que um valor válido seja informado.   
        while True:
            descricao = input('Descrição sobre o Bug: ').strip()
            if descricao == '':
                print('Erro! A descrioção não pode estar vazia.')  
            else:
                bug['descricao'] = descricao
                break
        # Exibe as opções de prioridade e valida a escolha do usuário.
        while True:
            print('\nEscolha a prioridade')
            print('1 - Alta')
            print('2 - Média')
            print('3 - Baixa')
            prioridade = input('Digite uma opção: ')
            if prioridade == '1':
                bug['prioridade'] = 'Alta'
                break
            elif prioridade == '2':
                bug['prioridade'] = 'Média'
                break
            elif prioridade == '3':
                bug['prioridade'] = 'Baixa'
                break
            else:
                print('Opção inválida.')
        bug['status'] = 'Aberto'
        bugs.append(bug)
        salvar_bugs(bugs)

# Exibe todos os bugs cadastrados.
def listar_bugs(bugs):
    # Verifica se existem bugs cadastrados.
    if not bugs:
        print('Nenhum bug cadastrado.')
        return
    # Exibe cabelçalho da listagem.
    print('='*20)
    print('BUGS CADASTRADOS')
    print('='*20)
    print(f'Total de bugs cadastrados: {len(bugs)}')
    print()
    # Percorre a lista de exibe as informações de cada bug.
    for i, bug in enumerate(bugs):
        print(f'=- BUG {i+1} -=')
        for campo, dado in bug.items():
            print(f'{campo}: {dado}')
        print('-'*20)

bugs = carregar_bugs()

continuar = True

# Loop principal do sistema.
while continuar:
    print('='*15)
    print('- Bug Traker -')
    print('='*15)
    print('1 - Cadastrar Bug')
    print('2 - Listar Bugs')
    print('3 - Buscar Bug')
    print('4 - Alterar status')
    print('5 - Remover Bug')
    print('6 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_bug(bugs)
        print('\nBug cadastrado com sucesso.')

    elif opcao == '2':
        listar_bugs(bugs)

    elif opcao == '3':
        print('Opção em desenvolvimento')

    elif opcao == '4':
        print('Opção em desenvolvimento')

    elif opcao == '5':
        print('Opção em desenvolvimento')

    elif opcao == '6':
        # Solicita confirmação antes de encerrar o programa.
        while True:
            resposta = input('Deseja realmente sair? [S/N]: '). strip().upper()
            if resposta == '':
                print('Digine S ou N.')
            else:
                resposta = resposta[0]
                if resposta == 'S':
                    print('Saindo...')
                    continuar = False
                    break
                elif resposta == 'N':
                    print('Operação Cancelada.')
                    break
    else:
        print('Opção inválida.')
print('Programa finalzado.')
