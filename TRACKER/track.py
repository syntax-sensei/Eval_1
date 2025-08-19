from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, time
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from enum import Enum

app = FastAPI()


class Macro_tags(str, Enum):
    protein = "protein"
    carbs = "carbs"
    fats = "fats"


class Track(BaseModel):
    user_id: int
    workout_id: int
    date: str
    sets: int
    reps: int
    weights: float
    calories_burned: int

class Nutrition(BaseModel):
    user_id: int
    date: str
    meals: list[str] = []
    calories: int 
    macronutrients: Macro_tags

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/workouts/")
def register(track: Track, session: SessionDep) -> Track:
    session.add(track)
    session.commit()
    session.refresh(track)
    return track

@app.post("/diet/")
def register(nutrition: Nutrition, session: SessionDep) -> Nutrition:
    session.add(nutrition)
    session.commit()
    session.refresh(nutrition)
    return nutrition






