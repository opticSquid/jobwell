import pytest

from app.bootstrap.wiring import (
    ingestion_graph,
    vector_store,
)
from app.graph.shared.state import GraphState


@pytest.fixture
async def seeded_job():
    state = GraphState(
        raw_input={
            "company": "Test Company",
            "job_title": "Senior Java Engineer",
            "job_description": """
            Java
            Spring Boot
            Kafka
            PostgreSQL
            AWS
            """,
        }
    )

    result = await ingestion_graph.ainvoke(state)

    try:
        yield result
    finally:
        document_ids = [doc.document_id for doc in result["vector_documents"]]

        await vector_store.delete(document_ids)
