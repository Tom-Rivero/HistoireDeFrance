import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# Configure with environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
MODEL = os.getenv("MODEL", "openrouter/mistralai/mistral-medium-3-5")

# Set environment for LiteLLM
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY
os.environ["OPENROUTER_API_BASE"] = OPENROUTER_BASE_URL


def test_api() -> None:
    """Check if LLM API is working"""
    messages = [
        {"role": "user", "content": "Hi."},
    ]
    response = completion(
        model=MODEL,
        messages=messages,
        base_url=OPENROUTER_BASE_URL,
        max_tokens=1,
    )
    assert response is not None
