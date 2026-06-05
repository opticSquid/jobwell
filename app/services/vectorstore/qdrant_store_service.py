from qdrant_client import AsyncQdrantClient
from qdrant_client.models import (
    PointIdsList,
    PointStruct,
)

from app.domains.enums.document_type import DocumentType
from app.domains.enums.record_type import RecordType
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

        points = []

        for document in documents:
            points.append(
                PointStruct(
                    id=document.document_id,
                    vector=document.embedding,
                    payload={
                        "job_id": document.metadata.get("job_id"),
                        "company": document.metadata.get("company"),
                        "job_title": document.metadata.get("job_title"),
                        "document_type": document.document_type.value,
                        "record_type": document.record_type.value,
                        "source_document_id": document.source_document_id,
                        "content": document.content,
                        "skills": document.metadata.get(
                            "skills",
                            [],
                        ),
                        "keywords": document.metadata.get(
                            "keywords",
                            [],
                        ),
                        "seniority": document.metadata.get("seniority"),
                        "years_experience": document.metadata.get("years_experience"),
                        "metadata": document.metadata,
                    },
                )
            )

        await self._client.upsert(
            collection_name=self._collection_name,
            points=points,
            wait=True,
        )

    async def search(
        self,
        embedding: list[float],
        limit: int = 10,
    ) -> list[VectorDocument]:

        results = await self._client.query_points(
            collection_name=self._collection_name,
            query=embedding,
            limit=limit,
        )

        documents = []

        for point in results.points:
            payload = point.payload

            documents.append(
                VectorDocument(
                    document_id=str(point.id),
                    document_type=DocumentType(payload["document_type"]),
                    record_type=RecordType(payload["record_type"]),
                    source_document_id=payload["source_document_id"],
                    content=payload["content"],
                    embedding=[],
                    metadata=payload.get(
                        "metadata",
                        {},
                    ),
                    score=point.score,
                )
            )

        return documents

    async def delete(
        self,
        ids: list[str],
    ) -> None:

        await self._client.delete(
            collection_name=self._collection_name,
            points_selector=PointIdsList(points=ids),
            wait=True,
        )
