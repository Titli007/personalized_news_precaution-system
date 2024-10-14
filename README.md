
# NewsGuard.AI : Stay Informed

## Overview

NewsGuard.AI is a web application built with Streamlit that allows users to fetch real-time news articles based on a search query. 
It also provides a summary of the fetched news and offers precautionary steps based on the summary.

The app allows users to receive news directly in their email if they choose to provide one.

## Features

- Fetches real-time news based on user query.
- Provides summarized news along with precautionary steps.
- Optionally, sends the summary and detailed news report to the user's email.
- Displays the source name and image, with a link to the full news article.
- Fully asynchronous and efficient workflow.

## Folder Structure

The main file for the Streamlit frontend is `app.py`, and it coordinates with backend services for news fetching, summarization, and email services.

```
.
├── app.py                 # Main Streamlit app
├── news_manager           # Manages fetching and summarizing news
│   ├── news_fetcher.py    # Fetches news from APIs
│   └── news_summerizer.py # Summarizes fetched news
├── email_sender           # Manages sending emails
│   └── send_email.py      # Handles email sending
├── config                 # Configuration files
│   └── config.py          # Contains sensitive information like API keys
├── .env                   # Environment variables for API keys and email
└── README.md              # Readme file (this file)
```

## Environment Variables

To securely manage API keys and sensitive information like email credentials, create a `.env` file in the root of your project with the following content:

```
# News API Key
GEMINI_API_KEY=your-api-key-here

# Email Configuration
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
APP_PASSWORD=your-app-specific-password
```

- **GEMINI_API_KEY**: This is your API key for fetching news from the external news service.
- **MAIL_USERNAME**: The email address from which news summaries will be sent.
- **MAIL_PASSWORD**: The password for the email account (use an app-specific password for better security).
- **APP_PASSWORD**: Use your app-specific password for email

## Requirements

To run the project, you need the following:

- Python 3.x
- Streamlit
- asyncio

You can install the required libraries by running:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Titli007/post_daily_news_app_assignment.git
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Visit the URL provided by Streamlit (usually `http://localhost:8501`) to interact with the application.

## Backend Configuration

- Make sure you have your backend properly set up, which handles fetching news from APIs and sending emails.

## Deployment

You can deploy the backend separately on platforms like Render or Heroku and run the Streamlit frontend on a separate service like Streamlit Cloud.

## License

This project is licensed under the MIT License.
