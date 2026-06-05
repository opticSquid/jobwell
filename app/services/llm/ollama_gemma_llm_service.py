import httpx

from app.services.llm.base import LLMService


class OllamaGemmaLLMService(LLMService):
    def __init__(
        self,
        host: str,
        model: str,
    ):
        self._host = host.rstrip("/")
        self._model = model

    async def generate(
        self,
        prompt: str,
    ) -> str:

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self._host}/api/generate",
                json={
                    "model": self._model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=360,
            )
            response.raise_for_status()

            payload = response.json()

            return payload["response"]
