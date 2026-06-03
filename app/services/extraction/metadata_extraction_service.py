from app.domains.models.extracted_metadata import ExtractedMetadata
from app.services.llm.base import LLMService


class MetadataExtractionService:
    def __init__(
        self,
        llm_service: LLMService,
        prompt_template: str,
    ):
        self._llm_service = llm_service
        self._prompt_template = prompt_template

    async def extract(
        self,
        job_description: str,
    ) -> ExtractedMetadata:
        raise NotImplementedError()
