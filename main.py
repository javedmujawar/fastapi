from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int
    password: str

class UserrResponse(BaseModel):
    name: str
    age: int 

@app.get("/user",response_model=UserrResponse)
def get_user():
    return {
        "name": "John Doe",
        "age": 30,
        "password": "secret"

    }