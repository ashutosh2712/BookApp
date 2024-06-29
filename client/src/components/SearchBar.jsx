const SearchBar = () => {
  return (
    <form className="navSearch">
      <input
        className="navSearchInput"
        type="text"
        name="author"
        value="author"
        placeholder="Search by author"
      />
      <input
        className="navSearchInput"
        type="text"
        name="genre"
        value="genre"
        placeholder="Search by genre"
      />
      <input
        className="navSearchInput"
        type="text"
        name="title"
        value="title"
        placeholder="Search by title"
      />
      <button type="submit" className="btn">
        Search
      </button>
    </form>
  );
};

export default SearchBar;
