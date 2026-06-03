from app.graph.shared.state import GraphState
from app.services.extraction.metadata_extraction_service import (
    MetadataExtractionService,
)


class ExtractMetadataNode:
    def __init__(
        self,
        extraction_service: MetadataExtractionService,
    ):
        self._service = extraction_service

    async def __call__(
        self,
        state: GraphState,
    ) -> GraphState:

        state.extracted_metadata = await self._service.extract(
            state.job_posting.job_description
        )

        return state
