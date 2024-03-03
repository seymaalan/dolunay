from typing import List
from fastapi import FastAPI,HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import Union 
import models
from pydantic import BaseModel
from starlette import status
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer
from database import engine, get_db
from datetime import date, time
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


class EventBase(BaseModel):
    event_name: str
    genre: str
    segment: str
    address: str
    city: str
    event_date: date
    event_time: time
    url: str

@app.get("/upcoming_events/")
def get_upcoming_events(db: Session = Depends(get_db)):
    current_date = date.today()
    upcoming_events = db.query(models.Event).filter(models.Event.event_date > current_date).all()
    return upcoming_events


@app.get("/past_events/")
def get_past_events(db: Session = Depends(get_db)):
    current_date = date.today()
    past_events = db.query(models.Event).filter(models.Event.event_date < current_date).all()
    return past_events

# Authentication Step

# This is not the db like in the pdf
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "is_admin": True,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "is_admin": False,
    },    
    "admin_user": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret3",
        "is_admin": True,
    },
}

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # login sayfasından ( /token/ url'sinden ) gönderilen (aşağıda login fonksiyonunda retun ettiğimiz şey) token, sanırım burda tutuluyor

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    is_admin: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username_yani_token: str): # eğer token'a username'i değil de başka bir şeyi atasaydık buraya o girilecekti. 
    if username_yani_token in db:
        user_dict = db[username_yani_token]
        return UserInDB(**user_dict)
        
def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

async def is_admin(token: Annotated[str, Depends(oauth2_scheme)]): 
# admin gerektiren işlevler (add, delete)bu fonksiyonu çağırıyor, bu fonksiyo ise oauth2_scheme'de tutulan token'ı alıyor ve validate ediyor.
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_admin:
        raise HTTPException(status_code=400, detail="Inactive user") 
    return user # token valid ise ilgili kullanıcıyı döndürüyor, döndürülen kullanıcı, admin gerektiren işlevlerde (add, delete)current_user olarak kullanılıyor


# The frontend (running in the user's browser) sends that username and password to a specific URL in our API (declared with tokenUrl="token").
# The API checks that username and password, and responds with a "token"
@app.post("/token")
# OAuth2PasswordRequestForm is a class dependency that declares a form body with:
# The username, The password. And other optional two things.
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):#form_data have the username and password which is provided by client in the "login"
    user_dict = fake_users_db.get(form_data.username) 
    if not user_dict: # checks username
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password: # checks password
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # By the spec, you should return a JSON with an access_token and a token_type
    return {"access_token": user.username, "token_type": "bearer"} # responds with a "token"

# Authentication Step is completed

@app.post("/add_event/")
async def add_event(event: EventBase, db: Session = Depends(get_db), current_user: dict = Depends(is_admin)):
    # Create a new event object
    new_event = models.Event(**event.dict())

    # Add the event to the database
    db.add(new_event)
    db.commit()

    return {"message": "Event added successfully"}

@app.delete("/delete_event/{event_name}")
async def delete_event(event_name: str,db: Session = Depends(get_db), current_user: dict = Depends(is_admin)):
    # Find the event in the database
    event = db.query(models.Event).filter(models.Event.event_name == event_name).first()

    # If event not found, raise HTTP 404 Not Found
    if not event:
        raise HTTPException(status_code=404, detail=f"Event with name {event_name} not found")

    # Delete the event from the database
    db.delete(event)
    db.commit()
    return {"message": f"Event with name {event_name} deleted successfully"}


