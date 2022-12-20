# APIs

This page shows you the methods, paths and input/output schema of all APIs in Watch Party.

## Movie queries

### Search for a movie based off the title

Searching for a movie based on the title returns the top five results. A request is sent to the Redis caching microservice which will return the query results from its NoSQL database or from TMDB.

* **Method**: `GET`
* **Path**: /api/movies/search/

Input:

```json
{
  "title": string,
}
```

Output:

```json
[
	{
		"tmdb_id": int,
		"title": string,
		"overview": string,
		"vote_count": int,
		"vote_average": int,
		"poster_path": string,
		"release_date": string
	},
]
```

### Get the top 20 trending movies

Make a request to this endpoint to receive basic info about the top 20 trending movies. A request is sent to the Redis caching microservice which will return the query results from its NoSQL database or from TMDB.

* **Method**: `GET`
* **Path**: /api/movies/popular/

Output:

```json
[
	{
		"tmdb_id": int,
		"title": string,
		"overview": string,
		"vote_count": int,
		"vote_average": int,
		"poster_path": string,
		"release_date": string
	},
]
```

### Get details about a movie

To get the details of a desired movie, search for it by its unique numerical `tmdb_id`. A request is sent to the Redis caching microservice which will return the query results from its NoSQL database or from TMDB.

* **Method**: `GET`
* **Path**: /api/movies/<int:tmdb_id>/

Output:

```json
{
  "tmdb_id": int,
  "title": string,
  "tagline": string,
  "overview": string,
  "vote_average": int,
  "vote_count": int,
  "runtime": int,
  "release_date": str,
  "genres": arr,
  "poster_path": str,
  "imdb_id": str,
}
```

## Genre endpoints

### List genres

This endpoint lists all genres. A request is sent to the movie Django microservice which queries it's PostgreSQL database.

* **Method**: `GET`
* **Path**: /api/genres/

Output:

```json
[
	{
		"id": 1,
		"name": "Action",
		"tmdb_id": 28
	},
]
```
## Get genre

This endpoint gets a desired genre from the id. A request is sent to the movie Django microservice which queries it's PostgreSQL database.

* **Method**: `GET`
* **Path**: /api/genres/<int:pk>/

Output:

```json
{
  "id": 1,
  "name": "Action",
  "tmdb_id": 28
}
```
