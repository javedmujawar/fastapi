from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str="abc"
# home route
@app.post("/create-user")
def create_user(name:str, age:int=0):
    return {"Name": name, "Age": age}

@app.post("/create-item")
def create_item(item:User):
    return {"message": "User Created", "date": item}

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address

@app.post("/create-user-with-address")    
def create_user_with_address(user: User):
    return user