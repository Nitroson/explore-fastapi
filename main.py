#Introduction

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message":"Hello Nitro Welcome to FASTAPI world"}


@app.get("/demo")
async def root():
    return {"Message":"Hello Nitro, I am a path demo"}


@app.get("/production")
async def root():
    return {"Message":"Hello Nitro , this is production page"}



#Query parameter 

from fastapi import FastAPI

app = FastAPI()


@app.get("/Hello")
async def hello(name:str,age = int):
    return{"name": name,"age":age}



# Datetime 
from fastapi import FastAPI
import datetime

app = FastAPI
@app.on_event("startup")
async def startup_event():
    print("Server started :", datetime.datetime.now())

@app.on_event("shutdown")
async def shutdown_event():
    print("server shutdown :", datetime.datetime.now())


#CRUD OPERATIONS
from fastapi import FastAPI

from pydantic import BaseModel
app =FastAPI()

data =[]

class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str

@app.post("/book")
def add_book(book: Book):
    data.append(book.dict())
    return data

@app.get("/list")
def get_book():
    return data


@app.delete("/book/{id}")
def delete_book(id :int):
    data.pop(id-1)
    return data 



#Pydantic api

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class student(BaseModel):
    id: int
    name: str
    subjects : list[str] = []

@app.post("/students/")
async def create_student(student:student):
    return {"Student" : student}


#Testing the API

test_student = {
    "id": 1,
    "name":"John Doe",
    "subject" : ["Math","Science"]

}

async def test_api():
    response = await create_student(test_student)
    print(response)


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"Message": "Hello I'm new here"} 

#Templates

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI , Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get("/hello/",response_class=HTMLResponse)
async def hello(request:Request):
    return templates.TemplateResponse( ("hello.html"), {"request": request})


#Static file
from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/hello{name}",response_class=HTMLResponse)
async def hello(request : Request, name:str):
    return templates.TemplateResponse("hello.html",{"request":request,"name":name})