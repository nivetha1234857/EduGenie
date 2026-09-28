@echo off
echo ==============================
echo       EduGenie Launcher
echo ==============================

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate
echo Installing/updating dependencies...
python -m pip install -r requirements.txt

if not exist .env (
    copy .env.example .env
    echo.
    echo IMPORTANT: Open .env and add your GEMINI_API_KEY.
    pause
)

echo Starting EduGenie...
python -m uvicorn main:app --reload
