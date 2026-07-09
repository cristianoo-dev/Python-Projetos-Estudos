print("Bem-vindo ao GameTracker!")

jogos = []

continuar = True

while continuar:
    print('='*20)
    print('=== Game Tracker ===')
    print('='*20)
    print('1 - Cadastrar jogo')
    print('2 - Listar jogos')
    print('3 - CBuscar jogo')
    print('4 - Alterar status')
    print('5 - Remover jogo')
    print('6 - Sair')
    print('='*20)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print("Funcionalidade em desenvolvimento.")

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
