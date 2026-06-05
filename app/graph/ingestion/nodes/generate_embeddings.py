from app.domains.enums.document_type import DocumentType
from app.domains.enums.record_type import RecordType
from app.domains.models.vector_document import (
    VectorDocument,
)
from app.graph.shared.state import GraphState
from app.services.embeddings.base import (
    EmbeddingService,
)


class GenerateEmbeddingsNode:
    def __init__(
        self,
        embedding_service: EmbeddingService,
    ):
        self._service = embedding_service

    async def __call__(
        self,
        state: GraphState,
    ) -> GraphState:

        documents = []

        summary_embedding = await self._service.embed_text(
            state.job_posting.job_description
        )

        base_metadata = state.extracted_metadata.model_dump()

        base_metadata["company"] = state.job_posting.company

        base_metadata["job_title"] = state.job_posting.job_title

        base_metadata["job_id"] = state.job_posting.job_id

        documents.append(
            VectorDocument(
                document_id=state.job_posting.job_id,
                document_type=DocumentType.JOB,
                record_type=RecordType.JOB_SUMMARY,
                source_document_id=state.job_posting.job_id,
                content=state.job_posting.job_description,
                embedding=summary_embedding,
                metadata=base_metadata,
            )
        )

        chunk_embeddings = await self._service.embed_texts(
            [chunk.content for chunk in state.chunks]
        )

        for chunk, embedding in zip(
            state.chunks,
            chunk_embeddings,
        ):
            documents.append(
                VectorDocument(
                    document_id=chunk.chunk_id,
                    document_type=DocumentType.JOB,
                    record_type=RecordType.JOB_CHUNK,
                    source_document_id=state.job_posting.job_id,
                    content=chunk.content,
                    embedding=embedding,
                    metadata=base_metadata,
                )
            )

        state.vector_documents = documents

        return state
