from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import User, Task

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    user = User(username=username, password = password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return {"error": "no user found"}
    
    if user.password != password: 
        return {"error": "wrong password"}
    
    return {"message": "ok", "user_id": user.id}

@app.post("/tasks")
def add_task(task: str, user_id: int, db: Session = Depends(get_db)):
    new_task = Task(task=task, user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks/{user_id}")
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id == user_id).all()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task: 
        db.delete(task)
        db.commit()
        return {"message": "deleted"}
    
    return {"error": "not found"}

@app.put("/tasks/{task_id}")
def mark_done(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task: 
        task.done = True
        db.commit()
        return task 
    
    return {"error": "not found"}