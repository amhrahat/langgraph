from tools.tool_building.arxiv import arxiv_tool
from tools.tool_building.duck import duckduckgo_tool
from tools.tool_building.wiki import wiki_tool
from llms.gemini import llm

tools = [arxiv_tool, duckduckgo_tool, wiki_tool]

llm_with_tools = llm.bind_tools(tools)