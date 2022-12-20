import React from "react";
import { useGetPopularQuery } from "../../store/moviesApi";
import MovieCard from "./MovieCard";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function MovieCardList() {
  const { data, error, isLoading } = useGetPopularQuery();

  if (isLoading) {
    return (
      <progress className="progress is-primary" />
    );
  }
  if (error) {
    console.log(error);
    return (
      <p>{error.error} --- {error.status}</p>
    );
  }

  return(
    <>
      <h1>
      Today's top movies
      </h1>
      <h3>{ error ? "ERROR!" : ""}</h3>
      <h3>{ data ? "Movies:" : "No movies found"}</h3>
      <Container fluid>

        {/* <Row>
          <Col>1</Col>
          <Col>2</Col>
          <Col>3</Col>
        </Row> */}

        { data.map(movie => (
            <MovieCard movie={movie} />
        ))}

      </Container>
    </>
  );
}

export default MovieCardList;
