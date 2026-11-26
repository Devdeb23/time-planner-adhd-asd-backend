import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") 

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

engine= create_engine(DATABASE_URL)
with Session(engine) as session:
    result = session.execute()


