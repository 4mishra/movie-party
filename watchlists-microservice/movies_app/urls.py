from django.urls import path
from .views import (
    list_movies_in_database,
    list_genres,
    detail_genre,
)


urlpatterns = [
    path("genres/", list_genres, name="genres_list_url"),
    path("genres/<int:pk>/", detail_genre, name="genre_detail_url"),
    path("movies/", list_movies_in_database, name="list_movies_in_database_url"),
]
