/* This is for the header part of our website. We have one header, divided
into four parts: the logo to the left, the search next to it, the three options next to it and then the checkout cart
*/
import React from "react";
import "./Header.css";
import SearchIcon from "@material-ui/icons/Search";
import ShoppingCartIcon from "@material-ui/icons/ShoppingCart";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <div className="header">
      <Link to="/">
      <img
        className="header__logo"
        src="http://pngimg.com/uploads/amazon/amazon_PNG11.png"
        alt="Amazon logo"
      />
      </Link>

      <div className="header__search">
        <input className="header__searchInput" type="text" />
        <SearchIcon className="header__searchIcon" />
      </div>

      <div className="header__nav">
        <div className="header__option">
          <span className="header__optionLineone">Hello User</span>
          <span className="header__optionLinetwo">Sign in</span>
        </div>

        <div className="header__option">
          <span className="header__optionLineone">Returns</span>
          <span className="header__optionLinetwo">& Orders</span>
        </div>

        <div className="header__option">
          <span className="header__optionLineone">Your</span>
          <span className="header__optionLinetwo">Prime</span>
        </div>
        <Link to='/checkout'>
        <div className="header__optionbasket">
          <ShoppingCartIcon className="header__basketIcon" />
          <span className="header__optionLinetwo header__basketCounter">0</span> 
        </div>
        </Link>
      </div>
    </div>
  );
}
