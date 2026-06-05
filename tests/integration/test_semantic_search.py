import pytest

from app.bootstrap.wiring import (
    semantic_search_service,
)


@pytest.mark.asyncio
async def test_semantic_search_returns_results(
    seeded_job,
):

    response = await semantic_search_service.search(
        query="Java Spring Boot Kafka",
        limit=5,
    )

    assert response is not None

    assert len(response.results) > 0
