from django.urls import path
from .views import (
    popular_movies,
    get_movie,
    search_movies,
)


urlpatterns = [
    path("movies/<int:tmdb_id>/", get_movie, name="movie_url"),
    path("movies/popular/", popular_movies, name="popular_movies_url"),
    path("movies/search/", search_movies, name="search_movies_url"),
]
