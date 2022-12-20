from rest_framework import serializers


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


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=300)
