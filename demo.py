import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "hello world !"

@app.get("/user")
def user():
    return {"user": "toto", "age": 21}

@app.api_route("/login", methods=("GET","POST","PUT"))
def login():
    return {"msg": "login success"}
