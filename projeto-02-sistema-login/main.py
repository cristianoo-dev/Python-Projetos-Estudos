# Credenciais cadastradas no sistema
usuario_cadastrado = 'admin'
senha_cadastrada = '1234'

print('==== LOGIN ====')

tentativas_restantes = 3

while True:
    usuario = input('Usuario: ').strip()
    senha = input('Senha: ').strip()

    # Não permite login com campos vazios
    if usuario == '' or senha == '':
         print('Usuário e senha são obrigatórios.')
         continue
                 
    if usuario != usuario_cadastrado and senha != senha_cadastrada:
        print('Usuário e senha incorretos')
        
    elif usuario != usuario_cadastrado:
        print('Usuário incorreto')
        
    elif senha != senha_cadastrada:
        print('Senha incorreta')
    
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print('Login realizado com sucesso!')
        break
       
    else:
        # Desconta uma tentativa após falha no login
        tentativas_restantes -= 1
        print ('=-'*10)
        # Encerra o programa quando as tentativas acabam
        if tentativas_restantes == 0:
            print('BLOQUEADO')
            break

        print('Tente Novamente')

        if tentativas_restantes >= 2:
            print(f'Restam {tentativas_restantes} tentativas.')

        if tentativas_restantes == 1:
            print('Resta 1 tentativa')   
