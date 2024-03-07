from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:150716@localhost:5432/gs'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

