from app.domains.dto.search_response import (
    SearchResponse,
    SearchResult,
)
from app.services.embeddings.base import (
    EmbeddingService,
)
from app.services.vectorstore.base import (
    VectorStore,
)


class SemanticSearchService:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_store: VectorStore,
    ):
        self._embedding_service = embedding_service
        self._vector_store = vector_store

    async def search(
        self,
        query: str,
        limit: int = 10,
    ) -> SearchResponse:

        query_embedding = await self._embedding_service.embed_text(query)

        documents = await self._vector_store.search(
            embedding=query_embedding,
            limit=limit,
        )

        return SearchResponse(
            results=[
                SearchResult(
                    document_id=d.document_id,
                    source_document_id=d.source_document_id,
                    content=d.content,
                    metadata=d.metadata,
                    score=d.score,
                )
                for d in documents
            ]
        )
