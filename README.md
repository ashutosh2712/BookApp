# BookApp

BookApp is a simple application to manage books with CRUD operations, allowing users to create, read, update, and delete books. Additionally, users can upload images for each book. This application uses FastAPI for the backend and supports integration with a frontend (such as a React app).

## Features

- Create a new book with an image upload
- Retrieve a list of books
- Retrieve details of a specific book
- Update book information
- Delete a book
- Serve uploaded images

## Installation

### Prerequisites

- Python 3.7+
- PostgreSQL (or any preferred database)
- `pip` (Python package installer)

### Setup

1. Clone the repository:

```sh
git remote add origin https://github.com/ashutosh2712/BookApp.git
cd BookApp
 cd client
  npm install
  npm run dev
 cd server
  pipenv install
  pipenv shell
  uvicorn main:app --reload


