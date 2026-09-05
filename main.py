from pydantic import BaseModel
from fastapi import FastAPI,status, HTTPException

app = FastAPI()

@app.post("/user",status_code= status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully"}

@app.get("/user")
def get_user():
    return {"message": "User retrieved successfully" , "status":"success"}
@app.get("/use2/{user_id}")
def get_user2(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User retrieved successfully" , "status":"success"}