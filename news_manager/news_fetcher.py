import asyncio
from duckduckgo_search import DDGS
from duckduckgo_search import AsyncDDGS

async def fetch_news(query):
    ddgs = AsyncDDGS()
    results =  await ddgs.anews(query, region='wt-wt', safesearch='off', timelimit='d', max_results=1)

    return results[0]
