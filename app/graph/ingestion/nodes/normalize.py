from app.domains.models.job_posting import JobPosting
from app.graph.shared.state import GraphState
from app.utils.ids import generate_uuid


def normalize(
    state: GraphState,
) -> GraphState:

    payload = state.raw_input

    state.job_posting = JobPosting(
        job_id=generate_uuid(),
        company=payload["company"].strip(),
        job_title=payload["job_title"].strip(),
        job_description=payload["job_description"].strip(),
        source=payload.get(
            "source",
            "manual",
        ),
    )

    return state
