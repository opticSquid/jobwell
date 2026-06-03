from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    qdrant_host: str = "localhost"

    qdrant_port: int = 6333

    ollama_host: str = "http://localhost:11434"

    llm_model: str = "gemma3"

    embedding_model: str = "bge-m3"

    class Config:
        env_file = ".env"


settings = Settings()
