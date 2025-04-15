from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Question(BaseModel):
	description: str
	options: List[str]
	correct_answer: str

@router.post("/", status_code=201)
def create_question(question: Question):
	return {"message": "Question created"}

