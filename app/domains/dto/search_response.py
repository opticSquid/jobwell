from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    document_id: str

    source_document_id: str

    content: str

    metadata: dict = Field(default_factory=dict)

    score: float | None = None


class SearchResponse(BaseModel):
    results: list[SearchResult] = Field(default_factory=list)
