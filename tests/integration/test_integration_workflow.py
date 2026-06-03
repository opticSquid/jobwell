import pytest

from app.bootstrap.wiring import (
    ingestion_graph,
)
from app.graph.shared.state import (
    GraphState,
)


@pytest.mark.asyncio
async def test_ingestion_workflow():

    state = GraphState(
        raw_input={
            "company": "Amazon",
            "job_title": "SDE II",
            "job_description": """
            Looking for Java, AWS,
            Kafka and Spring Boot
            experience.
            """,
        }
    )

    result = await ingestion_graph.ainvoke(state)

    assert len(result["vector_documents"]) > 0
