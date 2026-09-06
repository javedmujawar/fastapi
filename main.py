from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta,timezone

app = FastAPI()
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# create a function to generate a JWT token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

#login endpoint to generate a token
@app.post("/login")
def login(username: str, password: str):
    # In a real application, you would verify the username and password against a database
    if username == "test" and password == "test":
        token_data = {"sub": username}
        token = create_token(token_data)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
# token verification function
def verify_token(token: str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except: 
        raise HTTPException(status_code=401, detail="Invalid token")

# protected endpoint that requires a valid token
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return {"message": f"Hello, {username}. You have access to this protected route."}    
    