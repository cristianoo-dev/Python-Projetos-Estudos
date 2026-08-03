# Lista que armazena as tarefas do sistema
tarefas = []

print('='*20)
print('LISTA DE TAREFAS')
print('='*20)

continuar = True

# Loop principal do sistema (mantém o menu ativo)
while continuar:  
    print('''1 - Adionar Tarefa
2 - Listar Tarefas
3 - Sair''')
    # Adiciona nova tarefa após validação
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        # Remove espaços e impede tarefas vazias
        tarefa = input('Digite uma tarefa: ').strip()
        if tarefa == '':
            print('ERRO!!! A tarefa não pode estar vazia.')
            continue        
        tarefas.append(tarefa)
        print('Tarefa adicionada.')

    elif opcao == '2':
        if not tarefas:
            print('Nenhuma tarefa foi adicionada.')
        else:
            # Exibe tarefas com numeração
            for i, tarefa in enumerate(tarefas):
                print(f'{i + 1} - {tarefa}')

    # Confirma saída do sistema
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
    print('-'*20) 
print('Programa finalizado.')               
 