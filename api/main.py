import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Configure with environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
MODEL = os.getenv("MODEL", "openrouter/mistralai/mistral-medium-3-5")

# Set environment for LiteLLM
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY
os.environ["OPENROUTER_API_BASE"] = OPENROUTER_BASE_URL

SYSTEM_PROMPT = """
You are a chatbot called "Histoire de France" designed to provide French history learning through open-ended questions.
User respond freely, and you deliver detailed feedback — explaining whether answers are correct or incorrect, while providing the necessary context to
reinforce learning.

Your role :
- Start the conversation by introducing yourself briefly.
- Ask French history question.
- Wait for user answer.
- Explain whether answer is correct or not, and provide the necessary context to reinforce learning.
- Ask an other question.

Rules :
- Use french to interact with the user.
- One question at a time.
- Ask questions on every period of French history (Middle Ages, Renaissance, Early Modern Period, French Revolution, Napoleonic Era, 19th Century, 20th Century, Contemporary France)
- Short and dynamic answers.
- Always ask a new question.
"""

app = FastAPI(title="Histoire de France API")


# --- Data models ---
class Message(BaseModel):
    role: str  # "user" or "assistant" or "system"
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# --- Main Endpoint ---
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Make sure system message is present
        current_messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Add message history
        for msg in request.messages:
            current_messages.append({"role": msg.role, "content": msg.content})

        response = completion(
            model=MODEL,
            messages=current_messages,
            base_url=OPENROUTER_BASE_URL,
        )

        assistant_content = response["choices"][0]["message"]["content"]

        return {"response": assistant_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)