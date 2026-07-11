print("Bem-vindo ao GameTracker!")

def cadastrar_jogo():
        jogo = {}
        while True:
            nome_jogo = input('Nome do jogo: ').strip()
            if nome_jogo == '':
                print('ERRO! O nome do jogo não pode estar vazio.')
            else:
                jogo['Nome'] = nome_jogo
                break
        while True:
            plataforma = input('Plataforma: ').strip()
            if plataforma == '':
                print('ERRO! A plataforma não pode estar vazia.')
            else:
                jogo['Plataforma'] = plataforma
                break
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

jogos = []

continuar = True

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
        print("Funcionalidade em desenvolvimento.")

    elif opcao == '3':
        print("Funcionalidade em desenvolvimento.")

    elif opcao == '4':
        print("Funcionalidade em desenvolvimento.")

    elif opcao == '5':
        print("Funcionalidade em desenvolvimento.")

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

    print('-'*20) 
print('Programa finalizado.') 
