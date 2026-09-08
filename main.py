import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()


@app.get("/news")
def get_news(page: int = 1, limit: int = 10):
    url = "https://indianexpress.com/"
    response = requests.get(url)
    title = []
    soap = BeautifulSoup(response.text, "html.parser")
    for item in soap.find_all("span", class_="titleline"):
        title.append(item.text)
    start = (page - 1) * limit
    end = start + limit
    return {"page":page, "limit":limit, "total": len(title),"data": title[start,end]}
