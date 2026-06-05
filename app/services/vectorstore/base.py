from abc import ABC, abstractmethod

from app.domains.models.vector_document import VectorDocument


class VectorStore(ABC):
    @abstractmethod
    async def upsert(
        self,
        documents: list[VectorDocument],
    ) -> None:
        pass

    @abstractmethod
    async def search(
        self,
        embedding: list[float],
        limit: int = 10,
    ) -> list[VectorDocument]:
        pass

    @abstractmethod
    async def delete(
        self,
        ids: list[str],
    ) -> None:
        pass
