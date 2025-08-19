from pydantic import BaseModel
from enum import Enum
from datetime import datetime, time, date

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

class Exercise(BaseModel):
    exercise_name: str
    category: str
    equipment_needed: list[str] = []
    difficulty: str
    instructions: str
    target_muscles: str

