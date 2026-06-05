import json
from string import Template

from app.domains.models.extracted_metadata import ExtractedMetadata
from app.services.llm.base import LLMService


class MetadataExtractionService:
    def __init__(
        self,
        llm_service: LLMService,
        prompt_text: str,
    ):
        self._llm_service = llm_service
        self._prompt_text = prompt_text

    async def extract(
        self,
        job_description: str,
    ) -> ExtractedMetadata:

        template = Template(self._prompt_text)
        prompt = template.substitute(job_description=job_description)

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
