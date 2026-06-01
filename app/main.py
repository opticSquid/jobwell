from langgraph.graph import END, START, MessagesState, StateGraph

from nodes.mock_llm import mock_llm


def create_graph() -> StateGraph[MessagesState, None, MessagesState, MessagesState]:
    graph = StateGraph(MessagesState)
    graph.add_node("mock_llm", mock_llm)
    graph.add_edge(START, "mock_llm")
    graph.add_edge("mock_llm", END)
    return graph


def main():
    graph = create_graph()
    graph = graph.compile()
    graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})


if __name__ == "__main__":
    main()
