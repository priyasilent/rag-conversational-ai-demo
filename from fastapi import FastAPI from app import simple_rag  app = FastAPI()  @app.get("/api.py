from fastapi import FastAPI
from app import simple_rag

app = FastAPI()

@app.get("/ask")
def ask(query: str):
    return {"response": simple_rag(query)}
