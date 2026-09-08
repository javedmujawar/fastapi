import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup
import time

app = FastAPI()
# cache Store
cache_data = []
last_fetch = 0


@app.get("/news")
def get_news():
    global cache_data, last_fetch
    start = time.time()
    if time.time() - last_fetch > 60:
        print("Fetching fresh data")
        url = "https://news.ycombinator.com/"
        response = requests.get(url)
        soap = BeautifulSoup(response.text, "html.parser")
        cache_data = [item.text for item in soap.find_all("span", class_="titleline")]
        last_fetch = time.time()
    else:
        print("Catche data")

    end = time.time()
    time_taken = round(end - start)
    print(time_taken)
    return {"data": cache_data, "time_taken": time_taken}
