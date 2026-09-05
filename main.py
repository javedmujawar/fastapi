from fastapi import FastAPI

app = FastAPI()

# home route
@app.get("/users")
def home(name:str= None):
    return {"Name": name}

@app.get("/products")
def products(limit:int=10):
    return { "limit": limit}

@app.get("/items")
def items(name:str=None, price:int=0):
    return { "Name": name, "Price": price }