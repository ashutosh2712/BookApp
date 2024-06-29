# models.py
from sqlalchemy import Column, Float, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, index=True)
    genre = Column(String, index=True)
    image = Column(String, nullable=True)
    average_rating = Column(Float, nullable=True)