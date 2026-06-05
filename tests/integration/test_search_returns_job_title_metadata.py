import pytest

from app.bootstrap.wiring import (
    semantic_search_service,
)


@pytest.mark.asyncio
async def test_search_returns_job_title_metadata(
    seeded_job,
):

    response = await semantic_search_service.search(
        query="Kafka AWS",
        limit=5,
    )

    assert len(response.results) > 0

    first_result = response.results[0]

    assert "job_title" in first_result.metadata
