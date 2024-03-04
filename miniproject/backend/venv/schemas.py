from pydantic import BaseModel
from datetime import date, time


class PostBase(BaseModel):
    event_name: str | None = None
    genre: str | None = None
    segment: str | None = None
    address: str | None = None
    city: str | None = None
    local_date: date | None = None
    local_time: time | None = None
    url: str | None = None

    class Config:
        from_attributes = True


class CreatePost(PostBase):
    class Config:
        from_attributes = True
