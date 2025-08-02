from fastapi import FastAPI

from config.config import get_settings

from flashcard.routes import flashcard_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/config")
async def get_config():
    return {"config": get_settings()}

app.include_router(flashcard_router)