import React from "react";
import NavBar from "./NavBar";

function itemDetails() {
  return (
    <div>
      <header style={{ textAlign: "center" }}>
        <NavBar />
        <br />
        <br />
        <h2 id="itemTitle">PlayStation 5</h2>
        <body>
          <br />
          <br />
          <img
            src="data:image/jpeg;base64,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"
            id="itemImage"
            alt="item"
          />
          <br />
          <br />
          <span id="itemPrice">Price: $629.00</span>
          <br />
          <br />
          <a
            id="itemUrl"
            href="https://stockx.com/sony-ps5-playstation-5-digital-edition-console-white?country=US&currencyCode=USD&gclid=Cj0KCQiAnKeCBhDPARIsAFDTLTLqYPik6pZeLeiRP30WY9NjtlWDYMB_d4UTRRxWD_fQlRSV0F1ZOd0aAi50EALw_wcB"
          >
            Link to item
          </a>
          <br />
          <br />
          <span id="itemDescription">
            Play Has No Limits: PlayStation 5. The PS5 console unleashes new
            gaming possibilities that you never anticipated. Experience
            lightning fast loadi…
          </span>
          <br />
          <br />
          <button id="addWishlist" type="button">
            Add to my wishlist
          </button>
          <br></br>
        </body>
      </header>
    </div>
  );
}

export default itemDetails;
