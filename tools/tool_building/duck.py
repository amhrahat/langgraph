from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

@tool
def duckduckgo_tool(query: str) -> str:

    """This tool searches the latest news on DuckDuckGo for the given query and returns the results."""
    duck_search = DuckDuckGoSearchRun()
    return duck_search.invoke(query)