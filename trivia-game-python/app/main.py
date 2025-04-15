from fastapi import FastAPI
from app.routes.questions import router as questions_router

app = FastAPI()

app.include_router(questions_router, prefix="/questions")

@app.get("/")
def read_root():
	return {"message": "hola"}

