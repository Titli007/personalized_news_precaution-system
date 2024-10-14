import google.generativeai as genai
from config.config import GEMINI_API_KEY

def generate_summery(news):
    if GEMINI_API_KEY is None:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

    genai.configure(api_key=GEMINI_API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Context: You are tasked with summarizing the latest news and providing precautionary steps based on the summary. The context is as follows: {news}

    Instructions : 
    1. Summarize: Analyze the top news article fetched from the news section and provide a concise summary of 4 sentences bullet points that captures the main points of the article.
    2. Precautionary Steps: Based on the summary, list 3 precautionary steps that individuals should consider. Ensure that these steps are practical and relevant to the content of the news article.
    Format instructions : before summary there should be 2 new lines '\n\n', 2 headings should be in bold '##'
    """

    response = model.generate_content(prompt)
    print(response.text)

    return response.text
