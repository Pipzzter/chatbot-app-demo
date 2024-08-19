import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
HUGGINGFACE_BASE_URL = os.getenv('HUGGINGFACE_BASE_URL')


def initialize_openai_client():
    from openai import OpenAI
    return OpenAI(
        base_url=HUGGINGFACE_BASE_URL,
        api_key=HUGGINGFACE_API_KEY
    )
