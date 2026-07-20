from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "meu-projeto-fastapi"
    environment: str = "development"
    debug: bool = False
    database_url: str
    log_level: str = "INFO"
    cors_origins: list[str] = []
    openai_api_key: str


@lru_cache
def get_settings() -> Settings:
    # Falha rápido: se faltar uma variável obrigatória, a aplicação não sobe.
    return Settings()