from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/user", response_model=User)
def get_user():
    return User(id=1, name="John Doe") 