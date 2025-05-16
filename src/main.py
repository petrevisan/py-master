from fastapi import FastAPI
from src.routes import users

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

app.include_router(users.router)