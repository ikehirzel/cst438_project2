import React from "react";
<<<<<<< Updated upstream
=======
import NavBar from "./NavBar";
>>>>>>> Stashed changes

function CreateAccount() {
  return (
    <div style={{ textAlign: "center" }}>
<<<<<<< Updated upstream
=======
      <NavBar></NavBar>
>>>>>>> Stashed changes
      <br />
      <br />
      <header>
        <h2>Create Account</h2>
        <br />
        <br />
        <form>
          <input
            type="text"
            className="username"
            placeholder="Username"
          ></input>
          <br />
          <br />
          <input
            type="text"
            className="password"
            placeholder="password"
          ></input>
          <br /> <br />
          <button type="button" className="btn">
            Sign up
          </button>
        </form>
      </header>
    </div>
  );
}

export default CreateAccount;
