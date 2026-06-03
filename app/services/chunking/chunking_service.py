from uuid import uuid4

from app.domains.models.chunk import Chunk


class ChunkingService:
    def chunk_job_description(
        self,
        job_id: str,
        content: str,
        chunk_size: int = 1000,
        overlap: int = 100,
    ) -> list[Chunk]:

        chunks: list[Chunk] = []

        start = 0
        index = 0

        while start < len(content):
            end = start + chunk_size

            chunk_text = content[start:end]

            chunks.append(
                Chunk(
                    chunk_id=str(uuid4()),
                    job_id=job_id,
                    chunk_index=index,
                    content=chunk_text,
                )
            )

            index += 1
            start += chunk_size - overlap

        return chunks
