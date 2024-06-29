import { Link } from "react-router-dom";
import { books } from "../data/book";
const Books = () => {
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
