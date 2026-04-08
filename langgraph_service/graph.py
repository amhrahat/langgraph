from langgraph.graph import StateGraph, START, END
from langgraph_service.state import graph_schema
from langgraph_service.nodes import llm_node,tool_node
from langgraph_service.nodes.conditional_node import if_tool_call
from IPython.display import Image
from langchain_core.messages import HumanMessage


graph = StateGraph(graph_schema)

# Add nodes to the graph
graph.add_node("llm_node", llm_node)
graph.add_node("tool_node", tool_node)

# Add edges between nodes
graph.add_edge(START, "llm_node")
graph.add_conditional_edges("llm_node", if_tool_call,{"tool_node": "tool_node", "end": END})
graph.add_edge("tool_node", "llm_node")
graph.add_edge("llm_node", END)


react_graph = graph.compile()


Image(react_graph.get_graph().draw_mermaid_png())

response = react_graph.invoke({"messages": [HumanMessage(content="What is the latest news on AI?")]})
print(response['messages'][-1].content)