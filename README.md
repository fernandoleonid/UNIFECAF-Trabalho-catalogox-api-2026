# CatalogoX API

API REST interna desenvolvida para o gerenciamento de produtos utilizados por sistemas corporativos da empresa CatalogoX.

A aplicacao fornece operacoes basicas de cadastro, consulta, atualizacao e remocao de produtos, sendo utilizada como backend por ferramentas de estoque e precificacao.

---

## Funcionalidades

- Cadastro de produtos
- Listagem de produtos
- Atualizacao de produtos
- Remocao de produtos

A aplicacao funciona exclusivamente como API REST, nao possuindo interface grafica.

---

## Tecnologias Utilizadas

- Python 3
- Flask
- SQLite

---

## Estrutura do Projeto

catalogox-api/
|-- app.py
|-- catalogox.db
|-- requirements.txt
|-- README.md

---

## Como Executar a Aplicacao

1. Clonar o repositorio

git clone <url-do-repositorio>
cd catalogox-api

2. Instalar as dependencias

pip install -r requirements.txt

3. Executar a aplicacao

python app.py

A API estara disponivel em:

http://127.0.0.1:5000

Na primeira execucao, o banco de dados e inicializado automaticamente.

---

## Acesso a API

Todos os endpoints requerem autenticacao via header HTTP:

Authorization: usuario:senha

---

## Endpoints Disponiveis

- POST /produtos
- GET /produtos
- PUT /produtos/{id}
- DELETE /produtos/{id}

---

## Observacoes

- API desenvolvida para uso interno.
- Nao possui frontend.
- Projeto serve como base funcional para integracoes com outros sistemas.
