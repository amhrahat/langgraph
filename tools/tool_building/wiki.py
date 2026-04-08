from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool

@tool
def wiki_tool(query: str) -> str:
    """This tool searches Wikipedia for information on the given query and returns relevant results."""
    wiki_search = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return wiki_search.invoke(query)

