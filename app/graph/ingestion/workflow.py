from langgraph.graph import END, START, StateGraph

from app.graph.ingestion.nodes.chunk_document import ChunkDocumentNode
from app.graph.ingestion.nodes.extract_metadata import ExtractMetadataNode
from app.graph.ingestion.nodes.generate_embeddings import GenerateEmbeddingsNode
from app.graph.ingestion.nodes.normalize import normalize
from app.graph.ingestion.nodes.store_vectors import StoreVectorsNode
from app.graph.ingestion.nodes.validate import validate
from app.graph.shared.state import GraphState


def build_ingestion_workflow(
    extract_metadata_node: ExtractMetadataNode,
    chunk_document_node: ChunkDocumentNode,
    generate_embeddings_node: GenerateEmbeddingsNode,
    store_vectors_node: StoreVectorsNode,
):
    builder = StateGraph(GraphState)
    builder.add_node(
        "validate",
        validate,
    )

    builder.add_node(
        "normalize",
        normalize,
    )

    builder.add_node(
        "extract_metadata",
        extract_metadata_node,
    )

    builder.add_node(
        "chunk_document",
        chunk_document_node,
    )

    builder.add_node(
        "generate_embeddings",
        generate_embeddings_node,
    )

    builder.add_node(
        "store_vectors",
        store_vectors_node,
    )

    builder.add_edge(
        START,
        "validate",
    )

    builder.add_edge(
        "validate",
        "normalize",
    )

    builder.add_edge(
        "normalize",
        "extract_metadata",
    )

    builder.add_edge(
        "extract_metadata",
        "chunk_document",
    )

    builder.add_edge(
        "chunk_document",
        "generate_embeddings",
    )

    builder.add_edge(
        "generate_embeddings",
        "store_vectors",
    )

    builder.add_edge(
        "store_vectors",
        END,
    )
    graph = builder.compile()
    return graph
