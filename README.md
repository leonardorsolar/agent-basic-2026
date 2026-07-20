# meu-projeto-fastapi

"1 agente" (1 system prompt + 1 chamada ao modelo)

API em FastAPI que expõe um endpoint de chat integrado à API da OpenAI.

## Requisitos

- Python 3.14+
- [Poetry](https://python-poetry.org/)
- Uma chave de API da OpenAI

## Como baixar e executar

### 1. Instalar as dependências

```bash
poetry install
```

### 2. Configurar as variáveis de ambiente

Copie o arquivo de exemplo e preencha os valores (inclua sua `OPENAI_API_KEY`):

```bash
cp .env.example .env
```
Criar arquivo .env
Crie um arquivo .env na pasta do projeto:
```bash
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 3. Iniciar o servidor backend

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src
```

Você deve ver: `Uvicorn running on http://0.0.0.0:8000`

## Testando

### Passo 1: Servidor backend

Confirme que o backend está rodando (comando acima). A documentação interativa (Swagger) fica disponível em:

http://localhost:8000/docs

### Passo 2: Abrir o frontend (opcional)

Se você tiver um `index.html` de frontend, escolha uma opção:

- **Opção 1:** abra o `index.html` diretamente no navegador.
- **Opção 2:** sirva com um servidor HTTP simples:

```bash
python -m http.server 8080
```

### Passo 3: Testar o chat!

Abra o Swagger em http://localhost:8000/docs, clique em `POST /chat`, depois em **"Try it out"** e envie uma mensagem de teste:

```json
{
  "mensagem": "Explique o que é FastAPI",
  "modelo": "gpt-4.1-mini"
}
```

Clique em **Executar**.

Experimente fazer estas perguntas:

- "Olá! Como você funciona?"
- "Me conte uma curiosidade"
- "Explique Python em 3 linhas"

🎉 **Parabéns!** Se tudo funcionou, você criou seu primeiro ChatGPT! 🚀

## Rodando os testes automatizados

```bash
poetry run pytest
```
