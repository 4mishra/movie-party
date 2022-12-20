from rest_framework import serializers
from .models import Movie, Genre


class MovieModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "title",
            "tagline",
            "overview",
            "runtime",
            "release_date",
            "poster_path",
            "vote_average",
            "vote_count",
            "imdb_url",
            "genres",
            "id",
            "tmdb_id",
        ]
        depth = 1


class MovieListSerializer(serializers.Serializer):
    tmdb_id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    overview = serializers.CharField(max_length=2000)
    vote_count = serializers.IntegerField()
    vote_average = serializers.IntegerField()
    poster_path = serializers.CharField(max_length=299, allow_blank=True, default="")
    release_date = serializers.CharField(max_length=50, allow_blank=True, default="")


class ApiRequestMovieDetailSerializer(MovieListSerializer):
    tagline = serializers.CharField(max_length=300, allow_blank=True, default="")
    runtime = serializers.IntegerField()
    imdb_url = serializers.CharField(max_length=299, allow_blank=True, default="")
    genres = serializers.ListField()


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
            "tmdb_id",
        ]


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=300)
