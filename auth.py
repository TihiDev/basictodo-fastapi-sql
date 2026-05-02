import hashlib
from jose import jwt

SECRET = "secret123"
ALGORITHM = "HS256"


def hash_password(password: str):
    return hashlib.sha256((password + SECRET).encode()).hexdigest()

def verify_password(password: str, hashed: str):
    return hash_password(password) == hashed


def create_token(data: dict):
    return jwt.encode(data, SECRET, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])