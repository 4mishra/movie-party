import os
import json
import requests
import datetime
from .cache import Cache


class MovieRequests:
    TMDB_API_KEY = os.environ.get("TMDB_API_KEY_V3")
    base_url = "https://api.themoviedb.org/3/"
    lang = "language=en-US"

    def clean_movie_data(self, unfiltered_data, desired_fields):
        """
        Creates a new dictionary containing only the desired fields from the original
        """
        cleaned_movie = {}
        cleaned_movie["tmdb_id"] = unfiltered_data.get("id")
        for field in desired_fields:
            cleaned_movie[field] = unfiltered_data.get(field)
        return cleaned_movie

    def make_request(self, url, desired_fields=None, many=True):
        """
        Queries TMDB and calls helper function to filter to only desired fields.

        Returns a tupe containing an integer and one or many movies
        """
        response = requests.get(url)
        if response.status_code == 200:
            unfiltered_data = json.loads(response.content)
            if many:
                desired_fields = [
                    "title",
                    "overview",
                    "release_date",
                    "vote_count",
                    "vote_average",
                    "poster_path",
                ]
                data = [
                    self.clean_movie_data(movie, desired_fields)
                    for movie in unfiltered_data["results"]
                ]
            else:
                data = self.clean_movie_data(unfiltered_data, desired_fields)
        else:
            data = self.check_400_status_code(response.status_code)
        return (response.status_code, data)

    def check_400_status_code(self, status_code):
        if status_code == 401:
            return "This request was declined due to an unauthorized request. Make sure you have added your TMDB api key to the .env file."  # noqa: E501
        elif status_code == 404:
            return "The resource you are looking for could not be located."

    def get_popular_movies(self, cache=Cache()):
        """
        Retrieves data for top 20 trending movies from cache or TMDB.
        Returns tuple containing an integer and a list of movies.
        """
        status_code, data = cache.query("popular")
        if status_code != 200:
            url = f"{self.base_url}movie/popular?api_key={self.TMDB_API_KEY}&{self.lang}&page=1&region=US"  # noqa: E501
            status_code, data = self.make_request(url)
            if 200 <= status_code < 300:
                cache.add("popular", data, expiration=datetime.timedelta(hours=24))
        return status_code, data

    def search_tmdb_for_movie_query(self, query, cache=Cache()):
        """
        Searches cache or TMDB for movie based off string.
        Returns tuple containing an integer and a list of movies.
        """
        status_code, data = cache.query(
            query,
            reset_expiration=True,
            expiration_extension=datetime.timedelta(hours=24),
        )
        if status_code != 200:
            url = f"{self.base_url}search/movie?api_key={self.TMDB_API_KEY}&{self.lang}&query={query}&page=1&include_adult=false&region=US"  # noqa: E501
            status_code, data = self.make_request(url)
            if 200 <= status_code < 300:
                cache.add(query, data, expiration=datetime.timedelta(hours=24))
        return status_code, data

    # return details of one movie
    def get_movie_details(self, tmdb_id, cache=Cache()):
        """
        Searches cache or TMDB for a specific movie by it's ID.
        Returns tuple containing an integer and a dictionary.
        """
        status_code, data = cache.query(
            tmdb_id,
            reset_expiration=True,
            expiration_extension=datetime.timedelta(hours=24),
        )
        if status_code != 200:
            url = f"{self.base_url}movie/{tmdb_id}?api_key={self.TMDB_API_KEY}&{self.lang}"  # noqa: E501
            desired_fields = [
                "title",
                "tagline",
                "overview",
                "release_date",
                "vote_count",
                "vote_average",
                "poster_path",
                "imdb_id",
                "runtime",
                "budget",
                "genres",
            ]
            status_code, data = self.make_request(
                url, desired_fields=desired_fields, many=False
            )
            if 200 <= status_code < 300:
                cache.add(tmdb_id, data, expiration=datetime.timedelta(hours=24))

        return (status_code, data)
