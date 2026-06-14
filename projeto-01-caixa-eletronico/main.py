print('=' * 20)
print('CAIXA ELETRÔNICO')
print('=' * 20)

saldo = 1000
opção = 0
while opção != 4:
    print('1 - Consultar saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')

    opção = int(input('Escolha sua opção: '))

    if opção == 1:
        print(f'Seu saldo é igual a R${saldo:.2f} ')
    elif opção == 2:
        deposito = float(input(('Qual valor deseja depositar? R$')))
        saldo += deposito
        print('Deposito Realizado com Sucesso!')
        print(f'Saldo Atuazalido: R${saldo:.2f}')
    elif opção == 3:
        saque = float(input('Qual valor deseja sacar? R$'))
        if saque >  saldo:
            print('Saldo Insuficiente')
        else:
            saldo -= saque
            print(f'Saldo Atuzalido: R${saldo:.2f}')
    elif opção == 4:
        print('Saindo...')
    else:
        print('Opção Inválida')
    print('=-' *20)
