from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from database import Post, Base, engine
from datetime import date, datetime

class PostRequest(BaseModel):
    event_name: str
    genre: str
    segment: str
    address: str
    localdate: date
    local_time: datetime
    url: str

app = FastAPI()


@app.put("/item/{item_id}")
def update_item(item_id: int, item: PostRequest):
    return {"item_id": item.id, "item_name": item.event_name}
