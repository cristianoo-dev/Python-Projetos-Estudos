tarefas = []

print('='*20)
print('LISTA DE TAREFAS')
print('='*20)

print('''1 - Adionar Tarefa
2 - Listar Tarefas
3 - Sair''')

continuar = True

while continuar:    
    opção = input('Escolha uma opção: ')
    if opção == '1':
        tarefas.append(str(input('Digite a tarefa: ')))
        
    elif opção == '2':
        for i, tarefa in enumerate(tarefas):
            print(f'{i + 1} - {tarefa}')

    elif opção == '3':
        sair = ' '
        while sair not in 'SN':
            resposta = str(input('Deseja Realmente Sair? [S/N] ')).strip().upper()
            if resposta == '':
                print('Digite S ou N.')
            else:
                sair = resposta[0]
                if sair == 'S':
                    continuar = False
                    print('Saindo...')
