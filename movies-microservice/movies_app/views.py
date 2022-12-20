from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from .serializers import (
    MovieListSerializer,
    ErrorSerializer,
    ApiRequestMovieDetailSerializer,
)
from .acls import MovieRequests
import json
from dependency_injector.wiring import inject, Provide
from movies_project.container import Container


def prepare_json_response(status_code, data, serializer, many=True):
    if 200 <= status_code < 300:
        serialized_data = serializer(data, many=many)
        return Response(serialized_data.data, status=status_code)
    else:
        serialized_error = ErrorSerializer({"message": data})
        return Response(serialized_error.data, status=status_code)


# The class 'PopularMovieList' and function 'popular_movies'
# do the same thing and can be interchanged in the urls.
class PopularMovieList(APIView):
    def get(self, request, format=None, movie_requests=MovieRequests()):

        status_code, data = status_code, data = movie_requests.get_popular_movies()

        return prepare_json_response(
            status_code=status_code,
            data=data,
            serializer=MovieListSerializer,
        )


@api_view(["GET"])
@inject
def popular_movies(
    request, movie_requests: MovieRequests = Provide[Container.movie_search]
):
    status_code, data = movie_requests.get_popular_movies()

    return prepare_json_response(
        status_code=status_code,
        data=data,
        serializer=MovieListSerializer,
    )


@api_view(["GET"])
def get_movie(request, tmdb_id, movie_requests=MovieRequests()):
    status_code, data = movie_requests.get_movie_details(tmdb_id)

    return prepare_json_response(
        status_code=status_code,
        data=data,
        serializer=ApiRequestMovieDetailSerializer,
        many=False,
    )


@api_view(["GET"])
def search_movies(request, movie_requests=MovieRequests()):
    if request.body:
        query_dict = json.loads(request.body)
        try:
            query = query_dict["query"]
            status_code, data = movie_requests.search_tmdb_for_movie_query(query)

            return prepare_json_response(
                status_code=status_code,
                data=data,
                serializer=MovieListSerializer,
            )
        except KeyError:
            pass

    serialized_error = ErrorSerializer(
        {
            "message": "Please include a JSON body with request. Example: '{'query': 'star wars'}'"  # noqa: E501
        }
    )
    return Response(serialized_error.data, status=404)
