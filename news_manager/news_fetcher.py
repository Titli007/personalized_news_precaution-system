import asyncio
from duckduckgo_search import DDGS
from duckduckgo_search import AsyncDDGS

async def fetch_news(query):
    ddgs = AsyncDDGS()
    results =  await ddgs.anews(query, region='wt-wt', safesearch='off', timelimit='d', max_results=1)
    
    print(results[0])

    return results[0]

asyncio.run(fetch_news("weather in bengalore"))