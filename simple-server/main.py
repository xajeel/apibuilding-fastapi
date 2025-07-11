from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

user_list = [
    "sajeel",
    "ali",
    "malik"
]

class NewUser(BaseModel):
    username: str
    email: str

@app.get("/")
def home():
    return {"message": "Hello World"}


# === Path Prameters ===
@app.get("/greet/{name}")
def greeting(name: str):
    return {
        "message": f"Hello, {name}"
    }

# === Query Parameters ===
@app.get("/details")
async def get_details(username: str):
    if username in user_list:
        return {
            "message": f"Found User details abour {username}"
        }
    else:
        return HTTPException(status_code=402, detail=f"{username} not found")
    
# === Optional Parameters ===
@app.get("/greeting")
async def greetins(username:Optional[str] = "sajeel" ):
    return {
        "message": f"Hello {username} "
    }

# === Request Body ===
@app.post("/adduser")
async def add_user(user:NewUser):
    new_user = {
        "username": user.username,
        "email": user.email
    }

    user_list.append(new_user)

    return {
        "message": "New user Added",
        "user": new_user,
        "list": user_list
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",  port=8010 ,reload=True)