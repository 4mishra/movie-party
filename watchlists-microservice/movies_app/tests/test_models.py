from django.db import IntegrityError
from django.test import TestCase
from ..models import Genre, Movie
from .data.factory import GenreFactory
from .data.base_genre_data import base_name

# Create your tests here.


class GenreModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(
            name="Scary",
            tmdb_id=34,
        )

    def test_create_genre(self):
        genre = GenreFactory()
        self.assertIsInstance(genre, Genre)
        self.assertEqual(type(genre.tmdb_id), int)
        self.assertEqual(type(genre.name), str)
        self.assertIn(base_name, genre.__str__())
        try:
            self.assertIsNone(genre.title)
            self.assertIsNotNone(genre.id)
        except AttributeError:
            pass

    def test_create_invalid_genre(self):
        with self.assertRaises(IntegrityError):
            Genre.objects.create()
        with self.assertRaises(ValueError):
            Genre.objects.create(name=42, tmdb_id="not_a_number")

    def test_field_labels(self):
        genre = Genre.objects.get(tmdb_id=34)
        name_label = genre._meta.get_field("name").verbose_name
        tmdb_id_label = genre._meta.get_field("tmdb_id").verbose_name

        self.assertEqual(tmdb_id_label, "tmdb id")
        self.assertEqual(name_label, "name")

    def test_genre_name_max_length(self):
        genre = Genre.objects.get(tmdb_id=34)
        max_length = genre._meta.get_field("name").max_length
        self.assertEqual(max_length, 30)

    # def test_genres_populated_via_fixtures(self):
    #     file = open("../fixtures/genres.json")
    #     data = json.load(file)
    #     for item in data:
    #         Genre.objects.create(tmdb_id=item['pk'], name=item['fields']['name'])
    #     genres = Genre.objects.all()
    #     self.assertTrue(len(genres) > 15)


class MovieModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre1 = Genre.objects.create(
            name="Interesting",
            tmdb_id=3,
        )
        genre2 = Genre.objects.create(name="Not interesting", tmdb_id=4)
        movie = Movie.objects.create(
            title="Heavyweights",
            tmdb_id=314,
            runtime=121,
            poster_path="path/to/poster/2/",
        )
        movie.genres.add(genre1, genre2)
        movie.save()

    def test_setup(self):
        movie = Movie.objects.get(tmdb_id=314)
        self.assertTrue(len(movie.genres.all()) == 2)
        self.assertIsNotNone(movie)

    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Return of the King",
            tmdb_id=315,
            runtime=221,
            poster_path="path/to/poster/1/",
        )
        self.assertEqual(movie.title, "Return of the King")
        self.assertEqual(movie.tmdb_id, 315)
        self.assertEqual(movie.runtime, 221)
        self.assertEqual(movie.poster_path, "path/to/poster/1/")
        try:
            self.assertIsNone(movie.summary)
            self.assertIsNone(movie.id)
        except AttributeError:
            pass
        self.assertEqual(len(movie.genres.all()), 0)
        genre = Genre.objects.get(tmdb_id=3)
        movie.genres.add(genre)
        self.assertEqual(len(movie.genres.all()), 1)

    def test_field_labels(self):
        movie = Movie.objects.get(tmdb_id=314)
        title_label = movie._meta.get_field("title").verbose_name
        tmdb_id_label = movie._meta.get_field("tmdb_id").verbose_name

        self.assertEqual(tmdb_id_label, "tmdb id")
        self.assertEqual(title_label, "title")

    def test_create_invalid_movie(self):
        with self.assertRaises(IntegrityError):
            Movie.objects.create()
        with self.assertRaises(ValueError):
            Movie.objects.create(
                title=42, tmdb_id="not_a_number", runtime="not_a_number"
            )

    def test_movie_title_max_length(self):
        movie = Movie.objects.get(tmdb_id=314)
        max_length = movie._meta.get_field("title").max_length
        self.assertEqual(max_length, 150)

    def test_movie_runtime_field_can_be_null(self):
        movie = Movie.objects.get(tmdb_id=314)
        nullable = movie._meta.get_field("runtime").null
        self.assertEqual(nullable, True)

    def test_movie_str_method(self):
        movie = Movie.objects.get(tmdb_id=314)
        self.assertEqual(movie.__str__(), "Heavyweights")

    def test_movie_manager_get_or_save(self):
        result = Movie.objects.get_or_save(314, test=True)
        self.assertIsInstance(result, Movie)
        result = Movie.objects.get_or_save(1000, test=True)
        self.assertIsInstance(result, dict)
