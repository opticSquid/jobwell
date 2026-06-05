from pathlib import Path

from qdrant_client import AsyncQdrantClient

from app.config.constants import COLLECTION_NAME
from app.config.settings import settings
from app.graph.ingestion.nodes.chunk_document import ChunkDocumentNode
from app.graph.ingestion.nodes.extract_metadata import ExtractMetadataNode
from app.graph.ingestion.nodes.generate_embeddings import GenerateEmbeddingsNode
from app.graph.ingestion.nodes.store_vectors import StoreVectorsNode
from app.graph.ingestion.workflow import build_ingestion_workflow
from app.services.chunking.chunking_service import ChunkingService
from app.services.embeddings.ollama_bge_m3_embedding_service import (
    OllamaBGEM3EmbeddingService,
)
from app.services.extraction.metadata_extraction_service import (
    MetadataExtractionService,
)
from app.services.llm.ollama_gemma_llm_service import (
    OllamaGemmaLLMService,
)
from app.services.search.semantic_search_service import SemanticSearchService
from app.services.vectorstore.qdrant_store_service import (
    QdrantStoreService,
)

prompt = Path("app/prompts/metadata_extraction.txt").read_text()

qdrant_client = AsyncQdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port,
)

llm_service = OllamaGemmaLLMService(
    host=settings.ollama_host,
    model=settings.llm_model,
)

embedding_service = OllamaBGEM3EmbeddingService(
    host=settings.ollama_host,
    model=settings.embedding_model,
)

vector_store = QdrantStoreService(
    client=qdrant_client,
    collection_name=COLLECTION_NAME,
)

chunking_service = ChunkingService()

metadata_service = MetadataExtractionService(
    llm_service,
    prompt,
)

semantic_search_service = SemanticSearchService(
    embedding_service=embedding_service,
    vector_store=vector_store,
)


extract_metadata_node = ExtractMetadataNode(metadata_service)
chunk_document_node = ChunkDocumentNode(chunking_service)
generate_embeddings_node = GenerateEmbeddingsNode(embedding_service)
store_vectors_node = StoreVectorsNode(vector_store)


ingestion_graph = build_ingestion_workflow(
    extract_metadata_node,
    chunk_document_node,
    generate_embeddings_node,
    store_vectors_node,
)
