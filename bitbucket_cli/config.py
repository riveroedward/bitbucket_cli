import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BITBUCKET_ACCESS_TOKEN = os.getenv("BITBUCKET_ACCESS_TOKEN")
    BITBUCKET_API_URL = os.getenv("BITBUCKET_API_URL")
    BITBUCKET_USERNAME = os.getenv("BITBUCKET_USERNAME")

    @staticmethod
    def validate():
        if not Config.BITBUCKET_ACCESS_TOKEN:
            raise ValueError("BITBUCKET_ACCESS_TOKEN environment variable not set.")
