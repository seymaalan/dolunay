from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:150716@localhost/gs'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(Base):
    __tablename__ = "events_table"

    id = Column(Integer, primary_key=True, nullable=False)
    event_name = Column(String, nullable=False)
    genre = Column(String, nullable = False)
    segment = Column(String, nullable = False)
    address = Column(String, nullable = False)
    localdate = Column(Date)
    local_time = Column(TIMESTAMP(timezone=False), server_default=func.now())
    url = Column(String, nullable = False)