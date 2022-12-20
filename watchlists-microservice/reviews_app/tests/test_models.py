from django.test import TestCase
from .data.factory import UserRatingFactory, UserReviewFactory
from ..models import UserReview, UserRating
from watchlists_app.models import UserVO
from movies_app.models import Movie
from movies_app.tests.data.factory import MovieFactory
from watchlists_app.tests.data.factory import UserVOFactory
from datetime import datetime


class TestUserReviewModel(TestCase):
    def test_create(self):
        user = UserVOFactory()
        movie = MovieFactory()
        review_data = {
            "movie": movie,
            "user": user,
            "title": "Awesome Movie Review!",
            "content": "Fell asleep 5 mins in.",
        }
        review = UserReview.objects.create(**review_data)
        self.assertIsNotNone(review)
        self.assertIsInstance(review.date_created, datetime)
        self.assertIsInstance(review.date_updated, datetime)
        self.assertIsInstance(review.user, UserVO)
        self.assertIsInstance(review.movie, Movie)
        self.assertIsInstance(review.title, str)
        self.assertIsInstance(review.content, str)
        self.assertEqual(review.movie, movie)
        self.assertEqual(review.user, user)

    def test_str_method(self):
        review = UserReviewFactory()
        reviewer = review.user.username
        movie = review.movie.title
        title = review.title
        review_str = review.__str__()
        self.assertEqual(f"{title}: {movie} reviewed by {reviewer}", review_str)

    def test_fields_max_length(self):
        review = UserReviewFactory()
        max_title_length = review._meta.get_field("title").max_length
        max_content_length = review._meta.get_field("content").max_length
        self.assertEqual(max_title_length, 50)
        self.assertEqual(max_content_length, 10000)


class TestUserRatingModel(TestCase):
    def test_create(self):
        user = UserVOFactory()
        movie = MovieFactory()
        rating_data = {"movie": movie, "user": user, "score": 7}
        rating = UserRating.objects.create(**rating_data)
        self.assertIsNotNone(rating)
        self.assertIsInstance(rating.date, datetime)
        self.assertIsInstance(rating.user, UserVO)
        self.assertIsInstance(rating.movie, Movie)
        self.assertIsInstance(rating.score, int)
        self.assertTrue(0 < rating.score <= 10)
        self.assertEqual(rating.movie, movie)
        self.assertEqual(rating.user, user)

    def test_str_method(self):
        rating = UserRatingFactory()
        rater = rating.user.username
        movie = rating.movie.title
        score = rating.score
        rating_str = rating.__str__()
        self.assertEqual(f"{score}/10 for {movie} by {rater}", rating_str)

    def test_out_of_bounds_score(self):
        bad_scores = [-1, 11]
        for score in bad_scores:
            user = UserVOFactory()
            movie = MovieFactory()
            rating_data = {"movie": movie, "user": user, "score": score}
            self.assertRaises(TypeError, UserRating.objects.create(**rating_data))
