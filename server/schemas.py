
from pydantic import BaseModel
from typing import Optional
class BookBase(BaseModel):
    title: str
    author: str
    description: str
    genre : str
    average_rating: float = None ,
    image: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
