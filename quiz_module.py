import json
import re
from gemini_client import ask_gemini

def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def generate_quiz(passage: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.
Each question must have exactly 4 options and one correct answer.
Return ONLY valid JSON in this format:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{passage}
"""
    raw = ask_gemini(prompt)
    try:
        data = json.loads(clean_json_block(raw))
        if not isinstance(data, list):
            raise ValueError("Quiz response is not a list.")
        return data[:3]
    except Exception:
        return {
            "error": "Quiz generation returned an invalid format.",
            "raw_response": raw
        }
