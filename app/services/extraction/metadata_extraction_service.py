import json

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

        prompt = self._prompt_template.format(job_description=job_description)

        response = await self._llm_service.generate(prompt=prompt)

        payload = json.loads(response)

        return ExtractedMetadata(
            skills=payload.get("skills", []),
            keywords=payload.get("keywords", []),
            seniority=payload.get("seniority"),
            years_experience=payload.get("years_experience"),
            employment_type=payload.get("employment_type"),
            location=payload.get("location"),
            raw_extraction=payload,
        )
