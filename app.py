import streamlit as st
import asyncio
from news_manager.news_fetcher import fetch_news
from news_manager.news_summerizer import generate_summery
from email_sender.send_email import generate_email

# Custom CSS
custom_css = """
<style>
    .heading {
        color: white; 
        font-size: 29px; 
        margin: 30px;
    }
    .title {
        color: #4CAF50; 
        font-size: 36px; 
        text-align: center; 
    }
    .query-input {
        margin: 10px 0; 
        padding: 10px; 
        font-size: 16px; 
        border: 1px solid #ccc; 
        border-radius: 5px; 
    }
    .success {
        color: #4CAF50; 
    }
    .error {
        color: #f44336; 
    }
    .markdown-text {
        font-size: 18px; 
        line-height: 1.6; 
    }
</style>
"""

async def execute_workflow(query, user_email=None):
    try:
        # Fetch news asynchronously
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

def main():
    st.set_page_config(page_title="NewsGuard.AI : Stay Informed", layout="wide")
    
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("NewsGuard.AI : Stay Informed")

    # Input for query and email
    query = st.text_input("Enter your query:", placeholder="e.g., Weather in Bangalore")
    email = st.text_input("Enter your email (optional):", placeholder="e.g., example@example.com")

    if st.button("Fetch News"):
        if query:
            with st.spinner("Fetching and analyzing news..."):
                summary, source_name, source_url, news_image = asyncio.run(execute_workflow(query, email if email else None))

            if isinstance(summary, str) and source_name is None:
                st.error(summary, icon="🚫")
            else:
                st.success("News fetched successfully!", icon="✅")
                st.markdown(f"<div class='markdown-text'>\n{summary}</div>", unsafe_allow_html=True)
                if news_image:
                    st.image(news_image, width=400)
                st.markdown(f'<a href="{source_url}">Click here to read the full news</a>', unsafe_allow_html=True)
                st.markdown(f"<div><b>Source:</b> {source_name}</div>", unsafe_allow_html=True)

                if email:
                    st.info("A detailed report has been sent to your email.")
        else:
            st.warning("Please enter a query.", icon="⚠️")

if __name__ == "__main__":
    main()
