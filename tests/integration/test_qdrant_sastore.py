import pytest

from app.bootstrap.wiring import qdrant_client


@pytest.mark.asyncio
async def test_qdrant_health():

    collections = await qdrant_client.get_collections()

    assert collections is not None
