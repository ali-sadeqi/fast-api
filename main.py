from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
app = FastAPI() 


class Person(BaseModel):
    name : str 
    age : int 
    height : int 



@app.get('/api/')
def index(prs:Person):
    return 'i am learning fast api'