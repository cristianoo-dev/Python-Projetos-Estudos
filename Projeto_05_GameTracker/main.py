print("Bem-vindo ao GameTracker!")

# Cadastra um novo jogo solicitando as informações ao usuário.
def cadastrar_jogo():
        jogo = {}
        # Solicita o nome do jogo até que um valor válido seja informado.
        while True:
            nome_jogo = input('Nome do jogo: ').strip()
            if nome_jogo == '':
                print('ERRO! O nome do jogo não pode estar vazio.')
            else:
                jogo['Nome'] = nome_jogo
                break
        # Solicita a plataforma até que um valor válido seja informado.
        while True:
            plataforma = input('Plataforma: ').strip()
            if plataforma == '':
                print('ERRO! A plataforma não pode estar vazia.')
            else:
                jogo['Plataforma'] = plataforma
                break
        # Exibe as opções de status e valida a escolha do usuário.
        while True:
            print('\nEscolha o status')
            print('1 - Quero jogar')
            print('2 - Jogando')
            print('3 - Finalizado')
            print('4 - Abandonado')
            status = input('Digite uma opção: ')
            if status == '1':
                jogo['Status'] = 'Quero Jogar'
                break
            elif status == '2':
                jogo['Status'] = 'Jogando'
                break
            elif status == '3':
                jogo['Status'] = 'Finalizado'
                break
            elif status == '4':
                jogo['Status'] = 'Abandonado'
                break
            else:
                print('Opção inválida.')     
        return jogo

# Exibe todos os jogos cadastrados.
def listar_jogos():
    # Verifica se existem jogos cadastrados.
    if not jogos:
        print('Nenhum jogo cadastrado.')
        return
    # Exibe o cabeçalho da listagem.
    print('='*20)           
    print('JOGOS CADASTRADOS')
    print('='*20)
    print(f'Total de jogos cadastrados: {len(jogos)}')
    print()
    # Percorre a lista e exibe as informações de cada jogo.
    for i, jogo in enumerate(jogos):
        print(f'===== JOGO {i + 1} =====')
        for campo, dado in jogo.items():
            print(f'{campo}: {dado}')
        print()

# Busca um jogo pelo nome informado pelo usuário.
def buscar_jogo():
        # Solicita o nome do jogo até que um valor válido seja informado.
        while True:
            nome_busca = input('Digite o nome do jogo: ').strip()
            if nome_busca == '':
                print('ERRO! O nome do jogo não pode estar vazio.')
            else:
                break
        encontrou = False
        # Percorre a lista de jogos em busca de uma correspondência.
        for jogo in jogos:
            if nome_busca.casefold() == jogo['Nome'].casefold():
                encontrou = True
                print('JOGO ENCONTRADO')
                for campo, dado in jogo.items():
                    print(f'{campo}: {dado}')
                break
        # Informa caso nenhum jogo tenha sido encontrado.
        if not encontrou:
            print('Jogo não encontrado.')

# Altera o status de um jogo existente.
def alterar_status():
    # Solicita o nome do jogo até que um valor válido seja informado.
    while True:
        nome_jogo = input('Digite o nome do jogo: ').strip()
        if nome_jogo == '':
            print('ERRO! O nome do jogo não pode estar vazio.')
        else:
            break
    encontrou = False
    # Percorre a lista de jogos para encontrar o jogo informado.
    for jogo in jogos:
        if nome_jogo.casefold() == jogo['Nome'].casefold():
            encontrou = True
            print('JOGO ENCONTRADO')
            for campo, dado in jogo.items():
                print(f'{campo}: {dado}')
            # Exibe as opções de status e atualiza o jogo escolhido.
            while True:
                print('\nEscolha o novo status para o jogo')
                print('1 - Quero jogar')
                print('2 - Jogando')
                print('3 - Finalizado')
                print('4 - Abandonado')
                status = input('Digite uma opção: ')
                if status == '1':
                    jogo['Status'] = 'Quero Jogar'
                    break
                elif status == '2':
                    jogo['Status'] = 'Jogando'
                    break
                elif status == '3':
                    jogo['Status'] = 'Finalizado'
                    break
                elif status == '4':
                    jogo['Status'] = 'Abandonado'
                    break        
                else:
                    print('Opção inválida.')  
            print('Status do jogo atualizado com sucesso.')  
            break
    # Informa caso nenhum jogo tenha sido encontrado.     
    if not encontrou:
        print('Jogo não encontrado.')

# Remove um jogo cadastrado.
def deletar_jogo():
    # Solicita o nome do jogo até que um valor válido seja informado.
    while True:
        nome_remover = input('Digite o nome do jogo: ').strip()
        if nome_remover == '':
            print('ERRO! O nome do jogo não pode estar vazio.')
        else:
            break
    encontrou = False
    # Percorre a lista de jogos em busca do jogo informado.
    for jogo in jogos:
        if nome_remover.casefold() == jogo['Nome'].casefold():
            encontrou = True
            print('JOGO ENCONTRADO')
            for campo, dado in jogo.items():
                print(f'{campo}: {dado}')
            # Solicita a confirmação do usuário antes de remover o jogo.
            while True:
                resposta = input('Deseja realmente remover este jogo? [S/N] ').strip().upper()
                if resposta == '':
                    print('Digite S ou N.')
                else:
                    resposta = resposta[0]
                    if resposta == 'S':
                        jogos.remove(jogo)
                        print('Jogo deletado com sucesso.')
                        break
                    elif resposta == 'N':
                        print('Operação cancelada.')
                        break
            break
    # Informa caso nenhum jogo tenha sido encontrado.
    if not encontrou:
        print('Jogo não encontrado.')
     
jogos = []

continuar = True

# Loop principal do sistema.
while continuar:
    print('='*20)
    print('=== Game Tracker ===')
    print('='*20)
    print('1 - Cadastrar jogo')
    print('2 - Listar jogos')
    print('3 - Buscar jogo')
    print('4 - Alterar status')
    print('5 - Remover jogo')
    print('6 - Sair')
    print('='*20)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        jogo = cadastrar_jogo()
        jogos.append(jogo)
        print('\nJogo cadastrado com sucesso.')

    elif opcao == '2':
        listar_jogos()

    elif opcao == '3':
        buscar_jogo()

    elif opcao == '4':
        alterar_status()

    elif opcao == '5':
        deletar_jogo()

    elif opcao == '6':
        # Solicita confirmação antes de encerrar o programa.
        while True:
            resposta = input('Deseja realmente sair? [S/N] ').strip().upper()
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

    print('-'*20) 
print('Programa finalizado.')
