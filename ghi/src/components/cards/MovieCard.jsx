import React from "react";

function MovieCard({ movie }) {
  return (
    <div className="card">
      <h3 className="card-title">{movie.title} ({movie.release_date.slice(0,4)})</h3>
      <p className="card-body">{movie.vote_average}/10</p>
    </div>
  );
}

export default MovieCard;
