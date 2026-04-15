from tools.tool_building.arxiv import arxiv_tool
from tools.tool_building.clock import get_system_time
from tools.tool_building.duck import duckduckgo_tool
from tools.tool_building.wiki import wiki_tool
from llms.gemini_client import llm as gemini_llm
from llms.ollama_client import llm as ollama_llm

tools = [
    arxiv_tool,
    duckduckgo_tool,
    wiki_tool,
    get_system_time 
]

llm_with_tools = ollama_llm.bind_tools(tools)
# llm_with_tools = gemini_llm.bind_tools(tools)