from langgraph.graph import MessagesState


def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}
