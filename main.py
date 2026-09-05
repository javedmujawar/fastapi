from pydantic import BaseModel
from fastapi import FastAPI,status, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(HTTPException):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def handle_user_not_found(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"User '{exc.name}' not found.", "status":"error"},
    )


@app.get("/user/{name}")
def get_user(name: str):
    if name != "John":
        raise UserNotFoundException(name)
    return {name}
        
@app.get("/users/{user_id}")
def get_users(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User retrieved successfully"}
