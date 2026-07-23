from json_utils import carregar_bugs

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
        print('Opção em desenvolvimento')

    elif opcao == '2':
        print('Opção em desenvolvimento')

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
    print('-'*20)
print('Programa finalzado.')
