from database import Base
from sqlalchemy import Column, Integer, String, Boolean, text, Date,Time


class Event(Base):
    __tablename__ = "events"

    event_name = Column(String,primary_key=True)
    genre = Column(String)
    segment = Column(String)
    address = Column(String)
    city = Column(String)
    event_date = Column(Date)
    event_time = Column(Time(timezone=False))
    url = Column(String)
