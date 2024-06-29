import React from "react";
import SearchBar from "./SearchBar";
import { Link } from "react-router-dom";

const Navbar = ({ onSearch }) => {
  return (
    <nav className="navContainer">
      <Link to="/">
        <h2 className="titleContainer">BookApp</h2>
      </Link>
      <SearchBar onSearch={onSearch} />
      <div className="rightNav">SignIn</div>
    </nav>
  );
};

export default Navbar;
