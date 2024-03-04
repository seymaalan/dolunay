from database import Base
from sqlalchemy import Column, String, TIME, Date, Integer, text


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer,primary_key=True,nullable=False,server_default='None')
    event_name = Column(String,nullable=False,server_default='None')
    genre = Column(String,nullable=False,server_default='None')
    segment = Column(String,nullable=False,server_default='None')
    address = Column(String,nullable=False,server_default='None')
    city = Column(String,nullable=False,server_default='None')
    local_date = Column(Date,nullable=False,server_default='None')
    local_time = Column(TIME,nullable=False,server_default=text('now()'))
    url = Column(String,nullable=False,server_default='None')
