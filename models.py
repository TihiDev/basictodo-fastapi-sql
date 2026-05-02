from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base): 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Task(Base): 
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    done = Column(Boolean, default=False)
    user_id = Column(Integer)