from fastapi import FastAPI, Depends, HTTPException
from jose import JWTError
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import User, Task
from auth import hash_password, verify_password, create_token, decode_token

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ---------------- DB ----------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    user = User(
        username=username,
        hashed_password=hash_password(password)
    )

    db.add(user)
    db.commit()
    return {"message": "user created"}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="invalid credentials")

    token = create_token({"user_id": user.id})

    return {"access_token": token}

def get_user(token: str, db: Session):
    try:
        payload = decode_token(token)
        user_id = payload["user_id"]
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")

    user = db.query(User).filter(User.id == user_id).first()
    return user

@app.post("/tasks")
def add_task(task: str, token: str, db: Session = Depends(get_db)):
    user = get_user(token, db)

    new_task = Task(task=task, user_id=user.id)
    db.add(new_task)
    db.commit()

    return new_task

@app.get("/tasks")
def get_tasks(token: str, db: Session = Depends(get_db)):
    user = get_user(token, db)

    return db.query(Task).filter(Task.user_id == user.id).all()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, token: str, db: Session = Depends(get_db)):
    user = get_user(token, db)

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    if task:
        db.delete(task)
        db.commit()
        return {"message": "deleted"}

    return {"error": "not found"}