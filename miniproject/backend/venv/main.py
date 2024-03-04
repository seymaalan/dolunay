from fastapi import FastAPI
import sys
sys.path.append('/Users/elif/Desktop/dolunay/miniproject/backend/venv')
from database import engine
import models
from router import posts


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

models.Base.metadata.create_all(bind=engine)     

app.include_router(posts.router)