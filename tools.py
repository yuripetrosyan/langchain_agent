from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime



search = DuckDuckGoSearchRun()
#Create a search tool
search_tool = Tool(
    name = "search",
    func = search.run,
    description="Search the web for information"
)