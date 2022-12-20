from .app import clean_movie_data, check_400_status_code, search_tmdb
import os


def test_clean_all_movie_data_function_output():
    # Arrange
    fields_to_iterate_through = [
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
    input_dictionary = {
        "adult": False,
        "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
        "belongs_to_collection": None,
        "budget": 63000000,
        "genres": [{"id": 18, "name": "Drama"}],
        "homepage": "",
        "id": 550,
        "imdb_id": "tt0137523",
        "original_language": "en",
        "original_title": "Fight Club",
        "overview": 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.',  # noqa: E501
        "popularity": 0.5,
        "poster_path": None,
        "production_companies": [
            {
                "id": 508,
                "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
                "name": "Regency Enterprises",
                "origin_country": "US",
            },
        ],
        "release_date": "1999-10-12",
        "revenue": 100853753,
        "runtime": 139,
        "spoken_languages": [{"iso_639_1": "en", "name": "English"}],
        "status": "Released",
        "tagline": "How much can you know about yourself if you've never been in a fight?",  # noqa: E501
        "title": "Fight Club",
        "video": False,
        "vote_average": 7.8,
        "vote_count": 3439,
    }
    desired_output = {
        "tmdb_id": 550,
        "title": "Fight Club",
        "tagline": "How much can you know about yourself if you've never been in a fight?",  # noqa: E501
        "overview": 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.',  # noqa: E501
        "release_date": "1999-10-12",
        "vote_count": 3439,
        "vote_average": 7.8,
        "poster_path": None,
        "imdb_id": "tt0137523",
        "runtime": 139,
        "budget": 63000000,
        "genres": [{"id": 18, "name": "Drama"}],
    }

    # Act
    results = clean_movie_data(input_dictionary, fields_to_iterate_through)

    # Assert
    assert results == desired_output


def test_clean_movie_data_function_outputs():
    # Arrange
    input_dictionary = {
        "poster_path": "/cezWGskPY5x7GaglTTRN4Fugfb8.jpg",
        "adult": False,
        "overview": "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",  # noqa: E501
        "release_date": "2012-04-25",
        "genre_ids": [878, 28, 12],
        "id": 24428,
        "original_title": "The Avengers",
        "original_language": "en",
        "title": "The Avengers",
        "backdrop_path": "/hbn46fQaRmlpBuUrEiFqv0GDL6Y.jpg",
        "popularity": 7.353212,
        "vote_count": 8503,
        "video": False,
        "vote_average": 7.33,
    }
    desired_fields = [
        "title",
        "overview",
        "release_date",
        "vote_count",
        "vote_average",
        "poster_path",
    ]
    desired_output = {
        "tmdb_id": 24428,
        "title": "The Avengers",
        "overview": "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",  # noqa: E501
        "release_date": "2012-04-25",
        "vote_count": 8503,
        "vote_average": 7.33,
        "poster_path": "/cezWGskPY5x7GaglTTRN4Fugfb8.jpg",
    }

    # Act
    result = clean_movie_data(input_dictionary, desired_fields)

    # Assert
    assert result == desired_output


def test_check_400_status_code():
    # Arrange
    desired_result_401 = "This request was declined due to an unauthorized request. Make sure you have added your TMDB api key to the .env file."  # noqa: E501
    desired_result_404 = "The resource you are looking for could not be located"

    # Act
    result_401 = check_400_status_code(401)
    result_404 = check_400_status_code(404)
    result_500 = check_400_status_code(500)

    # Assert
    assert result_401 == desired_result_401
    assert result_404 == desired_result_404
    assert result_500 is None


def test_api_key_exists():
    assert os.environ.get("TMDB_API_KEY_V3") is not None


def test_search_tmdb_function():
    result = search_tmdb()
    assert result.find("SUCCESS") == 4
    assert result.find("<h1>FAIL") == -1
