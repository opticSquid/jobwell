from pydantic import BaseModel, Field


class ExtractedMetadata(BaseModel):
    skills: list[str] = Field(default_factory=list)

    keywords: list[str] = Field(default_factory=list)

    seniority: str | None = None

    years_experience: int | None = None

    employment_type: str | None = None

    location: str | None = None

    job_summary: str | None = None

    raw_extraction: dict = Field(default_factory=dict)
