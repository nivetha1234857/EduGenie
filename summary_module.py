from gemini_client import ask_gemini

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text for quick revision.
Keep the important facts.
Use short, clear bullet points and simple language.
Do not add information that is not present in the text.

Text:
{text}
"""
    return ask_gemini(prompt)
