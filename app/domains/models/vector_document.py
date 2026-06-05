from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.domains.enums.document_type import DocumentType
from app.domains.enums.record_type import RecordType
from app.utils.timestamps import utc_now


class VectorDocument(BaseModel):
    document_id: str

    document_type: DocumentType

    record_type: RecordType

    source_document_id: str

    content: str

    embedding: list[float]

    metadata: dict[str, Any] = Field(default_factory=dict)

    score: float | None = None

    created_at: datetime = Field(default_factory=utc_now)
