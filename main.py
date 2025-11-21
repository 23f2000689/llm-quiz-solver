from fastapi import FastAPI
from pydantic import BaseModel
from solver import solve_quiz
from task_handler import router as task_router

app = FastAPI(title="LLM Quiz Solver API")

app.include_router(task_router)

class QuizRequest(BaseModel):
    question: str
    options: list[str] | None = None
    context: str | None = None

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/solve")
def solve_route(data: QuizRequest):
    answer = solve_quiz(
        question=data.question,
        options=data.options,
        context=data.context
    )
    return {"answer": answer}
