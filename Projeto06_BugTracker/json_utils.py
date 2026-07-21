import json

def carregar_bugs():
    with open("bugs.json") as arquivo:
        bugs = json.load(arquivo)
    return bugs
