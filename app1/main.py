from typing import List

from fastapi import FastAPI
from sqlalchemy.orm import Session
import models
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine) # This will create the two models user and item.

app = FastAPI()

@app.get('/')
async def checking():
    return ("hello...........")