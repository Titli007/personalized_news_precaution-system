import streamlit as st
from workflow_manager.manage_workflow import execute_workflow
import asyncio


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


def main():
    st.set_page_config(page_title="NewsGuard.AI : Stay Informed", layout="wide")
    
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("NewsGuard.AI : Stay Informed")

    # Create a form to group the input and button together
    with st.form(key='news_form'):
        query = st.text_input("Enter your query:", placeholder="e.g., Weather in Bangalore")
        email = st.text_input("Enter your email (optional):", placeholder="e.g., example@example.com")
        submit_button = st.form_submit_button(label="Fetch News")

    # Only proceed when the form is submitted
    if submit_button:
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
