from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

app = FastAPI()

#Limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

#error Handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request:Request, exc:RateLimitExceeded):
    return JSONResponse(status_code=429,content={"details":"Too many request"})


#Rate Limiter  API
@app.get("/data")
@limiter.limit("5/minute")
def get_data(request:Request):
    return {"message":"Done"}
