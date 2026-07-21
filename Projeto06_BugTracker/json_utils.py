import json
from pathlib import Path

ARQUIVO_BUGS = Path(__file__).parent / "bugs.json"

def carregar_bugs():
    with open(ARQUIVO_BUGS) as arquivo:
        bugs = json.load(arquivo)

    return bugs
