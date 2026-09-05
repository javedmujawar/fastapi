from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# def common_logic():
#     # Common logic that can be reused across endpoints
#     return {"message": "This is common logic"}  

# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return {"endpoint": "home", "data": data}

# def get_current_user():
#     # Logic to get the current user
#     return {"user": "Javed"}

# @app.get("/profile")
# def profile(user=Depends(get_current_user)):
#     return {"endpoint": "profile", "user": user}

def verify_token(token: str=Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return {"message": "This is secure data", "user": user}