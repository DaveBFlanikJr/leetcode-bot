import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()
# DB
DB_URL = os.getenv("DATABASE_URL_STG")
print(DB_URL)

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Base
class Base(DeclarativeBase):
    pass
