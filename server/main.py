
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
import shutil
import books, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Directory to save uploaded images
UPLOAD_DIRECTORY = "uploaded_images"

# Create the directory if it doesn't exist
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


# Enable CORS
origins = [
    "http://localhost",
    "http://localhost:5173",  # React development server
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.Book)
def create_book( 
    title: str,
    author: str,
    description: str,
    average_rating: float,
    image: UploadFile = File(...),  # Image file
    db: Session = Depends(get_db)
):
    # Save the image to the UPLOAD_DIRECTORY
    image_path = os.path.join(UPLOAD_DIRECTORY, image.filename)
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Create the book with the image URL
    book_data = {
        "title": title,
        "author": author,
        "description": description,
        "average_rating": average_rating,
        "image": f"/images/{image.filename}"  # URL to access the image
    }
    return books.create_book(db=db, book=schemas.BookCreate(**book_data))

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_books = books.get_books(db, skip=skip, limit=limit)
    return db_books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = books.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = books.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = books.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
