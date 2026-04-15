from datetime import datetime
from langchain.tools import tool

@tool
def get_system_time() -> str:
    """Returns the current system date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")




