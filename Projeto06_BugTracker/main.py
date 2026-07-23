from json_utils import carregar_bugs, salvar_bugs

bugs = carregar_bugs()

novo_bug = {
    "titulo": "Teste",
    "descricao": "Teste de gravação",
    "prioridade": "Alta",
    "status": "Aberto"
}

bugs.append(novo_bug)

salvar_bugs(bugs)

print(bugs)