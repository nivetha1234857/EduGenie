from gemini_client import ask_gemini

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.
Organize it from Beginner to Intermediate to Advanced.
For each stage include:
- Topics to learn
- Suggested practice
- Useful resource types (videos, articles, books, documentation)
- A realistic sequence

Keep it practical and easy for a student to follow.

Topic:
{topic}
"""
    return ask_gemini(prompt)
