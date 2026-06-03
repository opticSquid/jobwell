import pytest

from app.bootstrap.wiring import llm_service


@pytest.mark.asyncio
async def test_gemma_generate():

    response = await llm_service.generate("Respond with only the word hello")

    assert response
