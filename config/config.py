from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the configuration variables from the .env file
GEMINI_API_KEY= os.getenv('GEMINI_API_KEY')

# Mail configuration
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
APP_PASSWORD = os.getenv('APP_PASSWORD')
