# Credenciais cadastradas no sistema
usuario_cadastrado = 'admin'
senha_cadastrada = '1234'

print('==== LOGIN ====')

tentativas_invalidas = 0

while True:
    
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print('Login realizado com sucesso!')
        break
       
    else:
        tentativas_invalidas += 1
        print('Tente Novamente')
        # Bloqueia o acesso após 3 erros 
        if tentativas_invalidas >= 3:
            print('BLOQUEADO')
            break
    