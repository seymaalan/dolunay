from fastapi import FastAPI,Depends
import sys
sys.path.append('/Users/elif/Desktop/dolunay/miniproject/backend/venv')
from database import engine,get_db
import models,schemas
from router import posts
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime



app = FastAPI()

models.Base.metadata.create_all(bind=engine)     

app.include_router(posts.router)

@app.get("/upcoming_events", response_model=List[schemas.CreatePost])
def get_upcoming_events(db: Session = Depends(get_db)):
    current_date = datetime.now()
    upcoming_events = db.query(models.Events).filter(models.Events.local_date >= current_date).all()

    return upcoming_events

@app.get("/past_events", response_model=List[schemas.CreatePost])
def get_past_events(db: Session = Depends(get_db)):
    current_date = datetime.now()
    past_events = db.query(models.Events).filter(models.Events.local_date < current_date).all()

    return past_events
