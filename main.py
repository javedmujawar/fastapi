import requests
from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url ="https://indianexpress.com/"
    response = requests.get(url)
    title=[]
    soap = BeautifulSoup(response.text,"html.parser")
    for item in soap.find_all("a",class_="topblockNews__featuredLink"):
        title.append(item)

    return title    
