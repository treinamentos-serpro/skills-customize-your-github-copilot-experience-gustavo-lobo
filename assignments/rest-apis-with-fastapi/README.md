# 📘 Atividade: APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI e modelos Pydantic. Você praticará métodos HTTP, parâmetros de rota, validação de dados e respostas de erro.

## 📝 Tarefas

### 🛠️ Criar o modelo e consultar livros

#### Descrição
Prepare o ambiente para executar a API e implemente as rotas de consulta do catálogo usando o código inicial fornecido.

#### Requisitos
O programa concluído deve:

- Instalar as dependências FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Executar a aplicação localmente com `uvicorn starter-code:app --reload`.
- Representar cada livro com um modelo Pydantic contendo `id`, `title` e `author`.
- Implementar `GET /books` para retornar todos os livros do catálogo.
- Implementar `GET /books/{book_id}` para retornar o livro correspondente ao identificador.
- Retornar o status HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Implementar operações de escrita

#### Descrição
Complete a API para permitir que clientes adicionem, atualizem e removam livros do catálogo.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para adicionar um livro enviado no corpo da requisição e responder com o livro criado e status HTTP `201`.
- Implementar `PUT /books/{book_id}` para substituir os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar o status HTTP `404` ao tentar atualizar ou remover um identificador inexistente.
- Manter as alterações disponíveis nas consultas enquanto a aplicação estiver em execução.
