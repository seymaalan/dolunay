from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from database import Post, Base, engine
from datetime import date, datetime
import models

class PostRequest(BaseModel):
    event_name: str
    genre: str
    segment: str
    address: str
    localdate: date
    local_time: datetime
    url: str

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: PostRequest):
    return {"item_id": item.id, "item_name": item.event_name}

