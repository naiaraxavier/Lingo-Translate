# Lingo Translate 🌍✨

**Lingo Translate** é uma ferramenta poderosa para tradução de textos entre vários idiomas. Desenvolvido com Python e Flask, é uma aplicação Server Side que permite aos usuários converter textos de uma língua para outra de forma eficiente e simples.

## Objetivo 🚀

O foco principal é oferecer uma ferramenta que possibilite a tradução rápida e confiável de textos entre diferentes idiomas. O projeto foi desenvolvido com ênfase nas seguintes habilidades e tecnologias:

### Habilidades Trabalhadas 💡

- Implementação de uma API utilizando arquitetura em camadas MVC.
- Utilização do Docker para projetos Python.
- Aplicação de conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Escrita de testes para APIs para garantir a implementação dos endpoints.
- Interação com um banco de dados não relacional MongoDB.
- Desenvolvimento de páginas web Server Side.

## Como Usar 🛠️

### Pré-requisitos

Certifique-se de ter o Python 3.x e o Docker instalados na sua máquina.

### Passos para Executar a Aplicação :rocket:

- **Usando Docker:**

    Certifique-se de ter o Docker instalado. Execute o seguinte comando para subir a aplicação:

    ```bash
    docker compose up translate
    ```

- **Executando Localmente:**

    Crie um ambiente virtual para o projeto:

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

    Instale as dependências necessárias:

    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```

    Inicie o servidor Flask:

    ```bash
    python3 src/app.py
    ```

## Acesso à Aplicação :globe_with_meridians:

Abra o navegador e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para visualizar a aplicação Lingo Translate.

## Contribuições 💪

### Desenvolvido por Mim

#### Arquivos e Pastas

- `src/translate_controller`
- `src/history_controller`
- `database/db.py`
- `models/language_model.py`
- `tests/admin/test_admin_controller.py`
- `tests/models/test_history_model.py`
- Alguns elementos em `src/views/template/index.html`

### Desenvolvido pela Trybe

A maior parte dos arquivos e pastas não mencionados como desenvolvidos por mim está relacionada ao desenvolvimento pela Trybe.


