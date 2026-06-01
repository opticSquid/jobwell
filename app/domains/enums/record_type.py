from enum import StrEnum


class RecordType(StrEnum):
    JOB_SUMMARY = "job_summary"
    JOB_CHUNK = "job_chunk"
    RESUME_SUMMARY = "resume_summary"
    RESUME_CHUNK = "resume_chunk"
