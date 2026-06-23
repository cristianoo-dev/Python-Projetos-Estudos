tarefas = []

print('='*20)
print('LISTA DE TAREFAS')
print('='*20)

print('''1 - Adionar Tarefa
2 - Listar Tarefas
3 - Sair''')

continuar = True

while continuar:    
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        tarefa = input('Digite uma tarefa: ').strip()
        if tarefa == '':
            print('ERRO!!! A tarefa não pode estar vazia.')
            continue        
        tarefas.append(tarefa)
        
    elif opcao == '2':
        if not tarefas:
            print('Nenhuma tarefa foi adicionada.')
        else:
            for i, tarefa in enumerate(tarefas):
                print(f'{i + 1} - {tarefa}')

    elif opcao == '3':
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
