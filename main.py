import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/posts")
def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="page not found")
    return response.json()
