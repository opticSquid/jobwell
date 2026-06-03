from qdrant_client import AsyncQdrantClient

from app.config.constants import COLLECTION_NAME
from app.config.settings import settings
from app.services.embeddings.ollama_bge_m3_embedding_service import (
    OllamaBGEM3EmbeddingService,
)
from app.services.llm.ollama_gemma_llm_service import (
    OllamaGemmaLLMService,
)
from app.services.vectorstore.qdrant_store_service import (
    QdrantStoreService,
)

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
