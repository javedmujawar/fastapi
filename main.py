from fastapi import FastAPI

app = FastAPI()

# home route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application."}

#users route
@app.get("/users")
def users():
    return {"users":["user1", "user2", "user3"]}

#about route
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id} 
