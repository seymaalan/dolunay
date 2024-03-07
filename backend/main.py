from typing import Union, List, Annotated
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import Base, engine, SessionLocal
from datetime import date, datetime
import models
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostRequest(BaseModel):
    event_name: str
    genre: str
    segment: str
    address: str
    localdate: date
    local_time: datetime
    url: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: PostRequest):
    return {"item_id": item.id, "item_name": item.event_name}

