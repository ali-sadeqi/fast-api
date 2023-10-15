from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session 
from database import engine , SessionLocal
from pydantic import BaseModel
import schemas , models
from fastapi.templating import Jinja2Templates
app = FastAPI() 

models.Base.metadata.create_all(bind= engine)
class Person(BaseModel):
    name : str 
    age : int 
    height : int 



@app.post('/createUser/' , schemas.User)
def create_user(user:schemas.UserCreate , db:Session = Depends(get_db)):
    db_user = db.query(models.User).filter(model.User.email==user.email)

    if db_user:
        raise HTTPException(status_code=400 , message="email already exists")
    
    user = models.User(email = user.email , password = user.password , username = user.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        dc.close()