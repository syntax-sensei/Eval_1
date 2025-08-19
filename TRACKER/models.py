from sqlalchemy import Column, Integre, String
from database import Base

class Workout(Base):
    __tablename__ = "workout_rec"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    nickname = Column(String)