from ...serializers import MovieListSerializer, ErrorSerializer

case_200 = {
    "status_code": 200,
    "data": [
        {
            "tmdb_id": 2,
            "title": "Something fun",
            "overview": "Once upon a time there was",
            "vote_count": 223,
            "vote_average": 8,
            "poster_path": "/api/poster/2/",
            "release_date": "2022-11-01",
        },
        {
            "tmdb_id": 3,
            "title": "Something else fun",
            "overview": "And then there was silence",
            "vote_count": 444,
            "vote_average": 3,
            "poster_path": "/api/poster/3/",
            "release_date": "2022-11-02",
        },
    ],
    "serializer": MovieListSerializer,
}

case_404 = {
    "status_code": 404,
    "data": {"message": "Resource not found"},
    "serializer": ErrorSerializer,
}
