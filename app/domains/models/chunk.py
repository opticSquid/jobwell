from pydantic import BaseModel


class Chunk(BaseModel):
    chunk_id: str
    job_id: str
    chunk_index: int
    content: str
