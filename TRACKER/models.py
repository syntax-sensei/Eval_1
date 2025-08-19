from sqlalchemy import Column, Integer, String
from database import Base

class Workout(Base):
    __tablename__ = "workout_rec"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, index=True)
    date = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weights = Column(Integer)
    calories_burned = Column(Integer)

