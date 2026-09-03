from fastapi import FastAPI

app = FastAPI()

# home route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}
