from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config.logger import configure_logging, logger
from app.config.settings import get_settings
from app.core.exceptions import AppError, app_error_handler

from pydantic import BaseModel
from openai import OpenAI
import os

settings = get_settings()
configure_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("startup", environment=settings.environment)

    yield

    logger.info("shutdown")

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(AppError, app_error_handler)


# @app.get("/")
# def read_root() -> dict[str, str]:
#     return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


# Inicializar cliente OpenAI
client = OpenAI(
    api_key=settings.openai_api_key
)

# Modelo de dados
class MensagemChat(BaseModel):
    mensagem: str
    modelo: str = "gpt-3.5-turbo"

# Rota principal
@app.get("/")
def inicio():
    return {
        "mensagem": "API ChatGPT funcionando! 🚀",
        "uso": "Envie POST para /chat"
    }

# Rota do chat
@app.post("/chat")
def conversar(dados: MensagemChat):
    try:
        resposta = client.chat.completions.create(
            model=dados.modelo,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente útil."
                },
                {
                    "role": "user",
                    "content": dados.mensagem
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return {
            "pergunta": dados.mensagem,
            "resposta": resposta.choices[0].message.content,
            "modelo_usado": dados.modelo
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro: {str(e)}"
        )