from datetime import datetime

from pydantic import BaseModel, Field

from app.utils.timestamps import utc_now


class IngestionJob(BaseModel):
    ingestion_id: str

    submitted_at: datetime = Field(default_factory=utc_now)

    total_jobs: int

    processed_jobs: int = 0

    failed_jobs: int = 0

    status: str = "PENDING"
