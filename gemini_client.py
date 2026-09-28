import os
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
except ImportError:
    genai = None

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

_client = None

if genai and API_KEY:
    _client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return plain text."""
    if not _client:
        return (
            "Gemini API is not configured. Please add your GEMINI_API_KEY "
            "to the .env file and restart the application."
        )

    try:
        response = _client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )
        text = getattr(response, "text", None)
        return text.strip() if text else "No response was returned by Gemini."
    except Exception as exc:
        return f"Gemini API error: {exc}"
