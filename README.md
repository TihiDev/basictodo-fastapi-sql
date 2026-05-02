# 🧠 Task Manager API (FastAPI + SQLite)

A simple backend project built with **FastAPI** and **SQLite**.  
It demonstrates basic CRUD operations, user handling, and database integration.

---

## 🚀 Features

- 👤 User registration
- 🔐 Simple login system
- ➕ Create tasks
- 📋 Get tasks by user
- ❌ Delete tasks
- ✅ Mark tasks as done
- 🗄️ SQLite database integration

---

## 🛠️ Tech Stack

- Python 🐍
- FastAPI ⚡
- SQLAlchemy 🗄️
- SQLite 💾

---

## 📁 Project Structure

backend/
│
├── main.py        # API routes
├── models.py      # Database models
├── database.py    # DB connection

---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/TihiDev/basictodo-fastapi-sql.git  
cd task-manager-api  

### 2. Install dependencies

pip install fastapi uvicorn sqlalchemy  

---

## ▶️ Run the project

python -m uvicorn main:app --reload  

Then open:

http://127.0.0.1:8000/docs  

---

## 📌 API Endpoints

### 👤 User
- POST /register → Create a user  
- POST /login → Login user  

### 📝 Tasks
- POST /tasks → Create a task  
- GET /tasks/{user_id} → Get user tasks  
- PUT /tasks/{task_id} → Mark task as done  
- DELETE /tasks/{task_id} → Delete task  

---

## 🧠 What I learned

- Building REST APIs with FastAPI  
- Working with databases using SQLAlchemy  
- CRUD operations  
- Basic backend architecture  

---

## ⚠️ Notes

- This is a learning project  
- No authentication tokens (JWT) yet  
- Passwords are stored in plain text (for learning only)  

---

## 📈 Future Improvements

- JWT authentication 🔐  
- Password hashing 🔑  
- Better project structure 📦  
- Frontend integration 🌐  

---

## 👨‍💻 Author

Built while learning backend development.
