#!/bin/bash
set -e

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

source venv/bin/activate
python -m pip install -r requirements.txt

if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "IMPORTANT: Open .env and add your GEMINI_API_KEY."
fi

python -m uvicorn main:app --reload
