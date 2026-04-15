# ERP AI Agent

A production-ready autonomous agent system built with LangGraph and LangChain. The system demonstrates end-to-end LLM application architecture including multi-model orchestration, tool integration, and state management for complex workflows.

## Overview

This project implements a ReAct-based agent that combines large language models with structured tools for information retrieval and decision-making. The agent follows a recursive pattern: reasoning about user queries, selecting appropriate tools, executing them, and refining responses based on results.

## Architecture

The system is organized around three core components:

### Graph-Based State Machine
The agent uses LangGraph's StateGraph to define deterministic workflow orchestration. This approach provides:
- **Explicit state transitions** through conditional routing
- **Composable node architecture** for clear separation of concerns
- **Deterministic execution** with reproducibility across runs
- **Visual representation** of agent flow for debugging and documentation

State flows through three primary nodes:
- **LLM Node**: Processes incoming messages and generates tool calls or responses
- **Tool Node**: Executes external function calls and processes results
- **Conditional Router**: Routes execution based on LLM decision output

### LLM Integration
The system supports multiple LLM backends:
- **Google Gemini** via LangChain's integration layer (primary)
- **Ollama** for local model deployment and offline capability

Both models are wrapped with tool-binding capabilities, enabling structured output for function calling.

### Tool System
The agent can access four tools for information retrieval and interaction:
- **Web Search**: DuckDuckGo integration for real-time information
- **Research Papers**: ArXiv API for academic content retrieval
- **Knowledge Base**: Wikipedia API for general reference
- **System Context**: Current time retrieval for temporal reasoning

Tools are defined as structured schemas that the LLM can invoke independently.

### API Layer
FastAPI provides REST endpoints for agent interaction. The service design ensures:
- Modern async request handling
- Modular router organization
- Clear separation between API and core logic

## Technology Stack

**Core Framework**:
- LangGraph 1.1+ - Stateful LLM application framework
- LangChain 1.2+ - LLM orchestration and tool binding

**LLM Providers**:
- Google Generative AI (Gemini model family)
- Ollama (local model inference)

**Web Framework**:
- FastAPI for HTTP API exposure
- Pydantic for schema validation and type safety

**Data Sources**:
- DuckDuckGo Search Integration
- ArXiv Research Repository
- Wikipedia Knowledge Base

**Dependencies**:
- LangChain Community Extensions (0.4+)
- Python 3.12+ (Type hints and modern language features)

## Project Structure

```
langgraph_service/
├── graph.py              # StateGraph definition and compilation
├── state.py              # TypedDict schema for agent state
└── nodes/
    ├── llm_node.py       # LLM decision-making logic
    ├── tool_node.py      # Tool execution and result processing
    └── conditional_node.py  # Conditional routing based on LLM output

llms/
├── gemini_client.py      # Google Gemini integration
└── ollama_client.py      # Ollama local model integration

tools/
├── tool_binding.py       # Tool schema and LLM binding
└── tool_building/        # Individual tool implementations
    ├── arxiv.py
    ├── duck.py
    ├── wiki.py
    └── clock.py
```

## Key Learnings

This project demonstrates practical solutions to:

1. **State Management in LLM Applications**: Managing conversation history and agent state through TypedDict schemas and graph-based execution patterns

2. **Dynamic Tool Selection**: Enabling LLMs to choose between tools based on query requirements through structured output binding and conditional routing

3. **Multi-Model Orchestration**: Abstracting LLM interfaces to support multiple backends without tight coupling

4. **Error Handling and Fallbacks**: Graceful degradation between primary (cloud) and secondary (local) model providers

5. **Production API Design**: Exposing agent capabilities through clean REST interfaces with proper async/await patterns

## Getting Started

### Prerequisites
- Python 3.12 or higher
- For cloud models: Google AI API key
- For local models: Ollama installation

### Installation

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### Configuration

Set environment variables:
```bash
export GOOGLE_API_KEY="your-google-ai-key"
# For local model usage, configure Ollama endpoint
```

### Running the Agent

```bash
# Start the FastAPI server
uvicorn main:app --reload

# Or invoke the graph directly
python -c "from langgraph_service.graph import react_graph; react_graph.invoke({'messages': [...]})"
```

## Design Patterns

### Conditional Routing
The agent uses LangGraph's conditional_edges for dynamic control flow:
```python
graph.add_conditional_edges(
    "llm_node", 
    if_tool_call,
    {"tool_node": "tool_node", "end": END}
)
```
This pattern enables the agent to decide between tool invocation and response generation on each reasoning step.

### Tool Binding
LLMs are enhanced with structured tool definitions:
```python
llm_with_tools = ollama_llm.bind_tools(tools)
```
This abstraction allows seamless switching between LLM providers while maintaining tool compatibility.

### State Updates
The graph maintains immutable state snapshots:
```python
state['messages'] = messages + [response]
```
This functional approach ensures clear data flow and easier debugging.

## Future Enhancements

- Implement agent memory and context management for multi-turn conversations
- Add observability and tracing for production monitoring
- Extend tool system with custom actions and integrations
- Implement streaming responses for real-time output

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629) - Agent reasoning framework

---

**Note**: This project prioritizes architectural clarity and learning outcomes over feature breadth. Each component is designed to be understood, modified, and extended.