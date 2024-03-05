from database import Base
from sqlalchemy import Column, String, TIME, Date, Integer


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer,primary_key=True,nullable=False)
    event_name = Column(String,nullable=False)
    genre = Column(String,nullable=False)
    segment = Column(String,nullable=False)
    address = Column(String,nullable=False)
    city = Column(String,nullable=False)
    local_date = Column(Date,nullable=False)
    local_time = Column(TIME,nullable=False)
    url = Column(String,nullable=False)
