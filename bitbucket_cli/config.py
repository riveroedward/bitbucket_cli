import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BITBUCKET_ACCESS_TOKEN = "ATBBq5VyMTXYuQstGa9VhTLxzuFk5BB5571C"
    BITBUCKET_API_URL = "https://api.bitbucket.org/2.0"
    BITBUCKET_USERNAME = "edwardriverop"

    @staticmethod
    def validate():
        if not Config.BITBUCKET_ACCESS_TOKEN:
            raise ValueError("BITBUCKET_ACCESS_TOKEN environment variable not set.")
