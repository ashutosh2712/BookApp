import { Link } from "react-router-dom";
// import { books } from "../data/book";
import axios from "axios";
import { useEffect, useState } from "react";

const Books = () => {
  const [books, setBooks] = useState([]);

  const fetchBooks = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/books`);
      setBooks(response.data);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <div className="booksContainer">
      <div className="booksList">
        {books.map((book) => (
          <Link to={`/books/${book._id}`} key={book._id}>
            <div className="bookGrid" key={book._id}>
              <img src={book.image} alt={book.title} className="bookImg" />
              <p>
                <b>Book :</b>
                {book.title}
              </p>
              <p>
                <b>Author :</b> {book.author}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Books;
