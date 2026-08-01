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
        descricao = input('Descrição sobre o bug: ').strip()
        if descricao == '':
            print('Erro! A descrição não pode estar vazia.')  
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
    # Exibe cabeçalho da listagem.
    print('='*20)
    print('BUGS CADASTRADOS')
    print('='*20)
    print(f'Total de bugs cadastrados: {len(bugs)}')
    print()
    # Percorre a lista e exibe as informações de cada bug.
    for i, bug in enumerate(bugs):
        print(f'=- BUG {i+1} -=')
        for campo, dado in bug.items():
            print(f'{campo}: {dado}')
        print('-'*20)

# Busca um bug pelo título informado pelo usuário.
def buscar_bug(bugs):
    # Busca um bug pelo título informado pelo usuário.
    while True:
        titulo_busca = input('Digite o título do bug: ').strip()
        if titulo_busca == '':
            print('ERRO! O título do bug não pode estar vazio.')
        else:
            break
    encontrou = False
    # Percorre a lista de bugs em busca de uma correspondência.
    for bug in bugs:
        if titulo_busca.casefold() == bug['titulo'].casefold():
            encontrou = True
            print('BUG ENCONTRADO')
            for campo, dado in bug.items():
                print(f'{campo}: {dado}')
            break
    # Informa caso nenhum bug tenha sido encontrado.
    if not encontrou:
        print('Bug não encontrado.')

# Altera o status de um bug existente.
def alterar_status(bugs):
    # Solicita título do bug até que um valor válido seja informado.
    while True:
        titulo_bug = input('Digite o título do bug: ').strip()
        if titulo_bug == '':
            print('ERRO! O título do bug não pode estar vazio.')
        else:
            break
    encontrou = False
    # Percorre a lista de bugs para encontrar o bug informado.
    for bug in bugs:
        if titulo_bug.casefold() == bug['titulo'].casefold():
            encontrou = True
            print('BUG ENCONTRADO')
            for campo, dado in bug.items():
                print(f'{campo}: {dado}')
            # Exibe as opções de status e atualiza o bug escolhido.
            while True:
                print('\nEscolha o novo status para o bug')
                print('1 - Aberto')
                print('2 - Em tratamento')
                print('3 - Fechado')
                status = input('Digite uma opção: ')
                if status == '1':
                    bug['status'] = 'Aberto'
                    break
                elif status == '2':
                    bug['status'] = 'Em tratamento'
                    break
                elif status == '3':
                    bug['status'] = 'Fechado'
                    break
                else:
                    print('Opção inválida.')
            print(f'Status atualizado para: {bug['status']}')
            salvar_bugs(bugs)
            break
        # Informa caso nenhum bug tenha sido encontrado
    if not encontrou:
        print('Bug não encontrado')   

# Remove um bug cadastrado.
def remover_bug(bugs):
    # Solicita o título do bug até que um valor valido seja informado.
    while True:
        titulo_remover = input('Digite o título do bug: ').strip()
        if titulo_remover == '':
            print('ERRO! O título do bug não pode estar vazio.')
        else:
            break
    encontrou = False
    # Percorre a lista de bugs em busca do bug informado.
    for bug in bugs:
        if titulo_remover.casefold() == bug['titulo'].casefold():
            encontrou= True
            print('BUG ENCONTRADO')
            for campo, dado in bug.items():
                print(f'{campo}: {dado}')
            # Solicita a confirmação do usuário de remover o bug.
            while True:
                resposta = input('Deseja realmente remover este bug? [S/N]').strip().upper()
                if resposta == '':
                    print('Digite S ou N.')
                else:
                    resposta = resposta[0]
                    if resposta == 'S':
                        bugs.remove(bug)
                        salvar_bugs(bugs)
                        print('Bug removido com sucesso.')
                        break
                    elif resposta == 'N':
                        print('Operação cancelada.')
                        break
            break
    # Informa caso nenhum bug tenha sido encontrado.
    if not encontrou:
        print('Bug não encontrado.')

bugs = carregar_bugs()

continuar = True

# Loop principal do sistema.
while continuar:
    print('='*15)
    print('- BugTraker -')
    print('='*15)
    print('1 - Cadastrar Bug')
    print('2 - Listar Bugs')
    print('3 - Buscar Bug')
    print('4 - Alterar Status')
    print('5 - Remover Bug')
    print('6 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_bug(bugs)
        print('\nBug cadastrado com sucesso.')

    elif opcao == '2':
        listar_bugs(bugs)

    elif opcao == '3':
        buscar_bug(bugs)

    elif opcao == '4':
        alterar_status(bugs)

    elif opcao == '5':
        remover_bug(bugs)

    elif opcao == '6':
        # Solicita confirmação antes de encerrar o programa.
        while True:
            resposta = input('Deseja realmente sair? [S/N]: ').strip().upper()
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
print('Programa finalizado.')
