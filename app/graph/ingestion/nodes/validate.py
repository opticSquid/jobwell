from app.graph.shared.state import GraphState


def validate(
    state: GraphState,
) -> GraphState:

    required_fields = [
        "company",
        "job_title",
        "job_description",
    ]

    for field in required_fields:
        if not state.raw_input.get(field):
            state.errors.append(f"{field} is required")

    return state
