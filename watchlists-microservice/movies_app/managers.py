from django.db.models.manager import Manager
import os
import requests
import json

MOVIES_HOST = os.environ.get("MOVIES_HOST", "movies:8002")


class CustomMovieManager(Manager):
    def get_or_save(self, movie_id, test=False):
        movie_query = self.filter(tmdb_id=movie_id)
        if len(movie_query) > 0:
            movie = movie_query[0]
        else:
            if not test:
                url = f"http://{MOVIES_HOST}/api/movies/{movie_id}/"
                response = requests.get(url=url)
                code = response.status_code
            else:
                code = 404
            if 200 <= code < 300:
                data = json.loads(response.content)
                movie_data = {
                    "tmdb_id": data["tmdb_id"],
                    "title": data["title"],
                    "runtime": data["runtime"],
                    "poster_path": data["poster_path"],
                }
                movie = self.create(**movie_data)
                try:
                    movie.genres.add(*[genre["id"] for genre in data["genres"]])
                except Exception as e:
                    return {"message": f"{e}: Unable to add movie genre."}
            else:
                return {
                    "message": f"Cannot get {movie_id} from db or api. Status: {code}"
                }
        return movie
