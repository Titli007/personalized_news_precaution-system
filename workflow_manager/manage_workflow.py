from news_manager.news_fetcher import fetch_news
from news_manager.news_summerizer import generate_summery
from email_sender.send_email import generate_email

async def execute_workflow(query, user_email=None):
    try:
        # Fetch news
        fetched_news = await fetch_news(query)
        
        if not fetched_news:
            raise ValueError("No news articles found for the given query.")

        # Extract source details and image from the fetched news
        source_name = fetched_news.get('source')
        source_url = fetched_news.get('url')
        news_image = fetched_news.get('image')
        
        # Generate news summary
        summary = generate_summery(fetched_news)
        
        if not summary:
            raise ValueError("Failed to generate a summary for the news.")

        # Prepare and send the email if user_email is provided
        if user_email:
            subject = "Personalized news precaution recommendation based on your search by NewsGuard.AI"
            result = generate_email(user_email, subject, summary, query)

            # Check if email was sent successfully
            if result:
                print("Workflow completed successfully!")
            else:
                print("Email sending failed.")

        return summary, source_name, source_url, news_image

    except Exception as e:
        print(f"An error occurred during the workflow: {e}")
        return str(e), None, None, None