from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    qdrant_host: str = "localhost"

    qdrant_port: int = 6333

    ollama_host: str = "http://localhost:11434"

    llm_model: str = "gemma4:e4b"

    embedding_model: str = "bge-m3:567m"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
