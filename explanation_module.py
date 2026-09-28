from gemini_client import ask_gemini

def explain_topic(topic: str) -> str:
    prompt = f"""
Explain the following topic like a patient teacher.
Use simple language.
Structure the answer as:
1. Simple definition
2. Main points
3. Simple example
4. One-line recap

Topic:
{topic}
"""
    return ask_gemini(prompt)
