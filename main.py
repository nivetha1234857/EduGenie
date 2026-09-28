from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie - AI Learning Assistant", version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")
@app.post("/qa")
async def qa(text: str = Form(...)):
    return JSONResponse({"result": answer_question(text)})


@app.post("/explain")
async def explain(text: str = Form(...)):
    return JSONResponse({"result": explain_topic(text)})


@app.post("/quiz")
async def quiz(text: str = Form(...)):
    return JSONResponse({"result": generate_quiz(text)})


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    return JSONResponse({"result": summarize_text(text)})


@app.post("/learn/recommendations")
async def recommendations(text: str = Form(...)):
    return JSONResponse({"result": get_learning_recommendations(text)})


@app.post("/api/task")
async def task_api(task: str = Form(...), text: str = Form(...)):
    handlers = {
        "qa": answer_question,
        "explain": explain_topic,
        "quiz": generate_quiz,
        "summarize": summarize_text,
        "recommend": get_learning_recommendations,
    }
    handler = handlers.get(task)
    if not handler:
        return JSONResponse({"error": "Invalid task selected."}, status_code=400)
    return JSONResponse({"result": handler(text)})
