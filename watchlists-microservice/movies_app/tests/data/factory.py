import factory
from ... import models
from .base_genre_data import base_name, base_tmdb_id
import random


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Genre

    name = factory.Sequence(lambda u: f"{base_name}%d" % u)

    @factory.sequence
    def tmdb_id(n):
        return base_tmdb_id - n


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Movie

    title = factory.Sequence(lambda u: "title_%d" % u)
    tmdb_id = factory.Sequence(lambda u: u)
    runtime = random.randint(80, 150)

    @factory.sequence
    def tmdb_id(n):
        return n

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for genre in extracted:
                self.genres.add(genre)
