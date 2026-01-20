from pytrends.request import TrendReq
from google_trends_mcp.config import config

def get_related_queries_logic(keyword: str, geo: str = None, timeframe_str: str = None):
    """
    Core logic for fetching related queries.
    """
    region = geo or config.get('default_region', 'US')
    
    # pytrends.request.TrendReq expects hl='en-US', tz=360 by default in this context
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], geo=region, timeframe=timeframe_str)
    
    related_queries = pytrends.related_queries()
    
    if keyword in related_queries:
        top_queries = related_queries[keyword]['top']
        rising_queries = related_queries[keyword]['rising']
        return {
            "top": top_queries.to_dict(orient='records') if top_queries is not None else [],
            "rising": rising_queries.to_dict(orient='records') if rising_queries is not None else []
        }
    return {"top": [], "rising": []}

def fetch_trending_keywords_tool(keyword: str, region: str = None, days: int = None) -> str:
    """
    Tool function to be registered with MCP.
    """
    days_val = days if days is not None else config.get('default_timeframe_days', 1)
    
    timeframe = f'now {days_val}-d' if days_val <= 7 else f'today {days_val//30}-m'
    if days_val == 0: timeframe = 'now 1-H'

    data = get_related_queries_logic(keyword, geo=region, timeframe_str=timeframe)
    return str(data)
