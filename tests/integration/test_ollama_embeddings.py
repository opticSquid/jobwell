import pytest

from app.bootstrap.wiring import embedding_service


@pytest.mark.asyncio
async def test_embedding_generation():

    embedding = await embedding_service.embed_text("Java Spring Boot Kafka")

    assert len(embedding) > 0
