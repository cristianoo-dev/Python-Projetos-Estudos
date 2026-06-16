usuario_cadastrado = 'admin'
senha_cadastrada = '1234'

print('==== LOGIN ====')

tentativa = 0

while True:
    
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print('Login realizado com sucesso!')
        break
        
    else:
        tentativa += 1
        print('Tente Novamente')
        if tentativa >= 3:
            print('BLOQUEADO')
            break
    