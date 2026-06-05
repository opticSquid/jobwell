from pydantic import BaseModel, Field

from app.domains.models.chunk import Chunk
from app.domains.models.extracted_metadata import ExtractedMetadata
from app.domains.models.job_posting import JobPosting
from app.domains.models.vector_document import VectorDocument


class GraphState(BaseModel):
    raw_input: dict = Field(default_factory=dict)

    job_posting: JobPosting | None = None

    extracted_metadata: ExtractedMetadata | None = None

    chunks: list[Chunk] = Field(default_factory=list)

    vector_documents: list[VectorDocument] = Field(default_factory=list)

    storage_result: dict = Field(default_factory=dict)

    errors: list[str] = Field(default_factory=list)
