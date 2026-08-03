# BugTracker

Sistema de gerenciamento de bugs desenvolvido em Python.

## Objetivo

Projeto criado para praticar organização de código, separação de responsabilidades e persistência de dados utilizando arquivos JSON.

O sistema simula uma ferramenta simples de controle de bugs, permitindo cadastrar, consultar, atualizar e remover registros.

## Funcionalidades

* Cadastro de bugs
* Listagem de bugs cadastrados
* Busca de bugs por título
* Alteração de status dos bugs
* Remoção de bugs com confirmação
* Validação de entradas do usuário
* Armazenamento permanente dos dados utilizando JSON
* Carregamento automático dos dados ao iniciar o sistema

## Conceitos praticados

* Funções
* Listas e dicionários
* Manipulação de arquivos JSON
* Criação de módulos em Python
* Importação de funções entre arquivos
* Separação de responsabilidades
* Organização de código
* Manipulação de dados persistentes

## Estrutura do projeto

```text
06-BugTracker
│
├── main.py
│   Código principal do sistema e menu de interação.
│
├── json_utils.py
│   Funções responsáveis por carregar e salvar os dados no arquivo JSON.
│
└── bugs.json
    Arquivo utilizado para armazenar os bugs cadastrados.
```

## Funcionamento

Ao iniciar o sistema, os dados cadastrados anteriormente são carregados automaticamente a partir do arquivo `bugs.json`.

Durante a utilização, o usuário pode cadastrar novos bugs, alterar informações e remover registros. Sempre que ocorre uma alteração, os dados são atualizados no arquivo JSON.

## Tecnologias utilizadas

* Python
* JSON
* Git
* GitHub
