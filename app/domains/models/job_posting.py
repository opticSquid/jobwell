from datetime import datetime

from pydantic import BaseModel, Field

from app.utils.timestamps import utc_now


class JobPosting(BaseModel):
    job_id: str
    company: str
    job_title: str
    job_description: str
    source: str = "manual"
    created_at: datetime = Field(default_factory=utc_now)
