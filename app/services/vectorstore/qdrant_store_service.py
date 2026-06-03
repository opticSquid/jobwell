from qdrant_client import AsyncQdrantClient

from app.domains.models.vector_document import VectorDocument
from app.services.vectorstore.base import VectorStore


class QdrantStoreService(VectorStore):
    def __init__(
        self,
        client: AsyncQdrantClient,
        collection_name: str,
    ):
        self._client = client
        self._collection_name = collection_name

    async def upsert(
        self,
        documents: list[VectorDocument],
    ) -> None:
        raise NotImplementedError()

    async def search(
        self,
        embedding: list[float],
        limit: int = 10,
    ) -> list[VectorDocument]:
        raise NotImplementedError()
