import React from "react";
import sharknado from '../Images/sharknado.jpg';

const MOVIES_URL = process.env.REACT_APP_MOVIES;
const WATCHLISTS_URL = process.env.REACT_APP_WATCHLISTS;

function TestHome() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the unbuilt Watch Parties frontend!</h1>
        <h3>Right now, the backend apis are being built so feel free to take a look at those!</h3>
        <img src={sharknado} className="App-logo" alt="logo" />
        <a
        className="App-link"
        href={`${MOVIES_URL}/api/movies/123/`}
        target="_blank"
        rel="noopener noreferrer"
        >
        Visit movie details endpoint to ensure functionality.
        </a>
        <br/>
        <a
        className="App-link"
        href={`${WATCHLISTS_URL}/admin/`}
        target="_blank"
        rel="noopener noreferrer"
        >
        Visit Django admin site to ensure genres successfully imported.
        </a>
      </header>
    </div>
  );
}

export default TestHome;
