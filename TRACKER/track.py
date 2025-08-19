from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query
from models import Base, Workout
from schemas import Track, Nutrition, Exercise
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    
    try:
        db = SessionLocal()
        yield db

    finally:
        db. close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/workouts/")
def register(track: Track) -> Track:
    db.add(track)
    db.commit()
    db.refresh(track)
    return track

@app.post("/diet/")
def register(nutrition: Nutrition) -> Nutrition:
    db.add(nutrition)
    db.commit()
    db.refresh(nutrition)
    return nutrition






