import streamlit as st

# Set the configuration variables from the .env file
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Mail configuration
MAIL_USERNAME = st.secrets["MAIL_USERNAME"]
MAIL_PASSWORD = st.secrets["MAIL_PASSWORD"]
MAIL_DEFAULT_SENDER = st.secrets["MAIL_DEFAULT_SENDER"]
APP_PASSWORD = st.secrets["APP_PASSWORD"]

# Print the GEMINI_API_KEY for debugging purposes (optional)
print(GEMINI_API_KEY)

