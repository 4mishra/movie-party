from flask import Flask
import os
import json
import requests

app = Flask(__name__)

TMDB_API_KEY_V3 = os.environ.get("TMDB_API_KEY_V3")
base_url = "https://api.themoviedb.org/3/"
query = "lord of the rings"
lang = "language=en-US"


def clean_movie_data(data, desired_fields):
    """
    Creates a new dictionary containing only the desired fields from the original
    """
    cleaned_movie = {}
    cleaned_movie["tmdb_id"] = data.get("id")
    for field in desired_fields:
        cleaned_movie[field] = data.get(field)
    return cleaned_movie


def check_400_status_code(status_code):
    if status_code == 401:
        return "This request was declined due to an unauthorized request. Make sure you have added your TMDB api key to the .env file."  # noqa: E501
    elif status_code == 404:
        return "The resource you are looking for could not be located"


@app.route("/moviesearch/search")
def search_tmdb():
    url = f"{base_url}search/movie?api_key={TMDB_API_KEY_V3}&{lang}&query={query}&page=1&include_adult=false&region=US"  # noqa: E501
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)

        desired_fields = [
            "title",
            "overview",
            "release_date",
            "vote_count",
            "vote_average",
            "poster_path",
        ]
        cleaned_movies = [
            clean_movie_data(movie, desired_fields) for movie in data["results"][:10]
        ]

        return f"<h1>SUCCESS</h1><p>This is simply a sampling of data from a request querying the lord of the rings: {cleaned_movies}</p>"  # noqa: E501
    else:
        data = check_400_status_code(response.status_code)
        return f"<h1>FAIL</h1><p>{data}</p><p>{response.status_code}</p>"


@app.route("/moviesearch/import/<int:id>")
def get_additional_movie_details(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY_V3}&{lang}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)

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
        cleaned_movie = clean_movie_data(data, desired_fields)
        return f"<h1>SUCCESS</h1><p>{cleaned_movie}</p>"

    else:
        data = check_400_status_code(response.status_code)
        return f"<h1>FAIL</h1><p>{data}</p>"


if __name__ == "__main__":
    app.run(debug=True)
