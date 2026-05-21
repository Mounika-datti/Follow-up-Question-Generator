import os
import requests

from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def generate_llm_followup(
    previous_question,
    candidate_answer,
    evaluation
):

    prompt = f"""
You are an AI technical interviewer.

Previous Question:
{previous_question}

Candidate Answer:
{candidate_answer}

Evaluation:
{evaluation}

Your task:
Generate ONE intelligent follow-up interview question.

Rules:
- Keep it relevant to the topic
- Ask about missing concepts
- Be professional
- Avoid repeating previous question
- Keep question concise
"""

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload
    )

    data = response.json()
    print(data)
    return data["choices"][0]["message"]["content"]