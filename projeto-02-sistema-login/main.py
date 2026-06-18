# Credenciais cadastradas no sistema
usuario_cadastrado = 'admin'
senha_cadastrada = '1234'

print('==== LOGIN ====')

tentativas_restantes = 3

while True:
    
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print('Login realizado com sucesso!')
        break
       
    else:
        tentativas_restantes -= 1

        if tentativas_restantes == 0:
            print('BLOQUEADO')
            break
        print ('=-'*10)
        print('Tente Novamente')
        print(f'Restam {tentativas_restantes} tentativas.')
    