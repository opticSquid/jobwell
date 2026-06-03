from app.graph.shared.state import GraphState
from app.services.chunking.chunking_service import (
    ChunkingService,
)


class ChunkDocumentNode:
    def __init__(
        self,
        chunking_service: ChunkingService,
    ):
        self._service = chunking_service

    async def __call__(
        self,
        state: GraphState,
    ) -> GraphState:

        state.chunks = self._service.chunk_job_description(
            state.job_posting.job_id,
            state.job_posting.job_description,
        )

        return state
