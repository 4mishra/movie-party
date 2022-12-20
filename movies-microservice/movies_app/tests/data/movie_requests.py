class FakeMovieRequests:
    movies = [
        {
            "tmdb_id": 0,
            "title": "Zero",
            "overview": "Nada",
            "vote_count": 0,
            "vote_average": 0,
            "poster_path": "zero/zero",
            "release_date": "10-10-1010",
        },
        {
            "tmdb_id": 1,
            "title": "One",
            "overview": "Ein",
            "vote_count": 1,
            "vote_average": 1,
            "poster_path": "one/one",
            "release_date": "12-12-1212",
        },
    ]

    movie_detail = {
        "tmdb_id": 1,
        "title": "One",
        "overview": "Ein",
        "vote_count": 1,
        "vote_average": 1,
        "poster_path": "one/one",
        "release_date": "12-12-1212",
        "tagline": "Es tut mir leid.",
        "runtime": 111,
        "imdb_url": "imdb/imdb",
        "genres": [1, 2, 3],
    }

    def get_popular_movies(self):
        status_code = 200
        return status_code, self.movies
