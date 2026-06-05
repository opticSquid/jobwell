import pytest

from app.bootstrap.wiring import (
    semantic_search_service,
)


@pytest.mark.asyncio
async def test_ingest_then_search(
    seeded_job,
):

    results = await semantic_search_service.search(
        query="Java Kafka AWS",
        limit=10,
    )

    assert len(results.results) > 0

    matching_results = [
        r for r in results.results if r.metadata.get("company") == "Test Company"
    ]

    assert len(matching_results) > 0
