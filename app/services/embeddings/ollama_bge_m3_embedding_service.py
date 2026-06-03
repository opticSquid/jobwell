import httpx

from app.services.embeddings.base import EmbeddingService


class OllamaBGEM3EmbeddingService(EmbeddingService):
    def __init__(
        self,
        host: str,
        model: str,
    ):
        self._host = host.rstrip("/")
        self._model = model

    async def embed_text(
        self,
        text: str,
    ) -> list[float]:

        embeddings = await self.embed_texts([text])

        return embeddings[0]

    async def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self._host}/api/embed",
                json={
                    "model": self._model,
                    "input": texts,
                },
                timeout=300,
            )

            response.raise_for_status()

            payload = response.json()

            return payload["embeddings"]
