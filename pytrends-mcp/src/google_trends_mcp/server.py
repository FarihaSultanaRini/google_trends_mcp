from mcp.server.fastmcp import FastMCP
from .tools.trends import fetch_trending_keywords_tool

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

