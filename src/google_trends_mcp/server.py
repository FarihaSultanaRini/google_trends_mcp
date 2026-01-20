import os
import sys

# Ensure the 'src' directory is in sys.path for direct execution
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from mcp.server.fastmcp import FastMCP
from google_trends_mcp.tools.trends import fetch_trending_keywords_tool

mcp = FastMCP("google-trends")

@mcp.tool()
async def fetch_trending_keywords(keyword: str, region: str = "US", days: int = 1) -> str:
    """
    Fetch top and rising related queries for a keyword.
    
    Args:
        keyword: The keyword to research.
        region: ISO country code (e.g., 'BD').
        days: Number of days to look back (converted to timeframe).
    """
    return fetch_trending_keywords_tool(keyword, region, days)

if __name__ == "__main__":
    mcp.run()

