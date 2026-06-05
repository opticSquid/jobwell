import pytest

from app.bootstrap.wiring import (
    semantic_search_service,
)


@pytest.mark.asyncio
async def test_search_returns_company_metadata(
    seeded_job,
):

    response = await semantic_search_service.search(
        query="Backend Engineer",
        limit=5,
    )

    assert len(response.results) > 0

    first_result = response.results[0]

    assert "company" in first_result.metadata
