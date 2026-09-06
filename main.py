import time
import asyncio
from fastapi import FastAPI

app = FastAPI()
# def task():
#     time.sleep(3)
#     return "Done"

# async def task():
#     await asyncio.sleep(3)
#     return "Done"

@app.get("/")
async def home():
    """demo of aysnc"""
    await asyncio.sleep(3)
    return "Done"