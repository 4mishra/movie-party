from django.test import TestCase
from ..views import prepare_json_response
from .data.views_test_data import case_200, case_404
from rest_framework.views import Response
from .data.movie_requests import FakeMovieRequests
from django.urls import reverse
import json
from movies_project import container


class TestPrepareJsonResponse(TestCase):
    def load_data(self, case):
        return {
            "status_code": case["status_code"],
            "data": case["data"],
            "serializer": case["serializer"],
        }

    def test_200_response_data(self):
        input_data = self.load_data(case_200)

        result = prepare_json_response(**input_data, many=True)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, Response)
        self.assertEqual(200, result.status_code)

    def test_400_response_data(self):
        input_data = self.load_data(case_404)

        result = prepare_json_response(**input_data, many=False)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, Response)
        self.assertEqual(404, result.status_code)


class TestPopularMoviesEndpoint(TestCase):
    def test_get_popular_movies(self):
        fake_movies = FakeMovieRequests()
        with container.movie_search.override(fake_movies):
            response = self.client.get(reverse("popular_movies_url"))
        data = json.loads(response.content)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) == len(fake_movies.get_popular_movies()[1]))
