from app.graph.shared.state import GraphState
from app.services.vectorstore.base import (
    VectorStore,
)


class StoreVectorsNode:
    def __init__(
        self,
        vector_store: VectorStore,
    ):
        self._store = vector_store

    async def __call__(
        self,
        state: GraphState,
    ) -> GraphState:

        await self._store.upsert(state.vector_documents)

        state.storage_result = {"stored_documents": len(state.vector_documents)}

        return state
