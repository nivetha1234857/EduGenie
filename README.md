# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant based on the supplied sample project document.

## Features

- Q&A – ask educational questions
- Explain – simplify difficult concepts
- Quiz – generate 3 MCQs with 4 options each
- Summary – summarize long educational text
- Learning Path – generate beginner-to-advanced recommendations

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Requirements

- Python 3.10+
- A Gemini API key

## Run on Windows

1. Open Command Prompt inside the EduGenie folder.
2. Create a virtual environment:

```bat
python -m venv venv
venv\Scripts\activate
```

3. Install packages:

```bat
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env`.
5. Open `.env` and replace the placeholder with your Gemini API key.
6. Start the project:

```bat
uvicorn main:app --reload
```

7. Open:

```text
http://127.0.0.1:8000
```

## Run on macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000.

## Important

Never upload your `.env` file or share your Gemini API key publicly.

## API endpoints

- POST `/qa`
- POST `/explain`
- POST `/quiz`
- POST `/summarize`
- POST `/learn/recommendations`
- POST `/api/task`

## Note about the supplied sample

The sample document describes Gemini 1.5 Pro and a local LaMini-Flan-T5-783M explanation module. This runnable version uses the current Google GenAI Python SDK and Gemini for all five tasks so the project stays lightweight and easy to run. The folder/module architecture and user-facing functionality follow the supplied EduGenie specification.
