from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Date, text

class Post(Base):
    __tablename__ = "events_table"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    event_name = Column(String, nullable=False)
    genre = Column(String, nullable = False)
    segment = Column(String, nullable = False)
    address = Column(String, nullable = False)
    localdate = Column(Date)
    local_time = Column(TIMESTAMP(timezone=False), server_default=text('now()'))
    url = Column(String, nullable = False)