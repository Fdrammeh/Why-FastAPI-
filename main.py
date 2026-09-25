from fastapi import FastAPI
from pydantic import BaseModel

# Create the application instance - this is your API
app = FastAPI()
class EchoRequest(BaseModel):
    message: str           
    shout: bool = False

# A GET "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to my first API"}
#GET /about
@app.get("/about/")
def about():
    return {
        "name":"Fatimah",
        "current Module":"FastAPI",
        "Fun_fact":"learning APIs!"
    }
        

# A GET /greet/{name}
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}! Welcome to my API."}
 

@app.post("/echo")
def echo_message(request: EchoRequest):
    message = request.message

    if request.shout:
        message = message.upper()