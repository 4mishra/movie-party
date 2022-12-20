from rest_framework import viewsets, permissions
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .serializers import (
    MovieModelDetailSerializer,
    GenreSerializer,
    ErrorSerializer,
)
from .models import Movie, Genre


def prepare_json_response(status_code, data, serializer, many=True):
    if 200 <= status_code < 300:
        serialized_data = serializer(data, many=many)
        return Response(serialized_data.data, status=status_code)
    else:
        serialized_error = ErrorSerializer({"message": data})
        return Response(serialized_error.data, status=status_code)


# The class 'GenreViewSet' and function 'list_genres'
# do the same thing and can be interchanged in the urls.
class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Genre.objects.all().order_by("name")
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


@api_view(["GET"])
def list_genres(request):
    genres = Genre.objects.all().order_by("name")
    serialized_genres = GenreSerializer(genres, many=True)
    return Response(serialized_genres.data, status=200)


@api_view(["GET"])
def detail_genre(request, pk):
    genre = Genre.objects.get(id=pk)
    serialized_genres = GenreSerializer(genre)
    return Response(serialized_genres.data, status=200)


@api_view(["GET", "POST"])
def list_movies_in_database(request):
    if request.method == "GET":
        movies = Movie.objects.all().order_by("title")
        serialized_movies = MovieModelDetailSerializer(movies, many=True)
        return Response({"movies": serialized_movies.data}, status=200)
    else:
        pass
