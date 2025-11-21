import asyncio
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import os
from quiz_solver import solve_quiz_chain

router = APIRouter()

API_SECRET = os.getenv("API_SECRET")

class TaskPayload(BaseModel):
    email: str
    secret: str
    url: str

@router.post("/task")
async def handle_task(req: Request):
    try:
        body = TaskPayload(**(await req.json()))
    except:
        raise HTTPException(status_code=400, detail="Invalid payload")

    if body.secret != API_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    asyncio.create_task(solve_quiz_chain(body.email, body.secret, body.url))
    return {"status": "accepted"}
