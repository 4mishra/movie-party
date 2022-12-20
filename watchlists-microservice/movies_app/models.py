from django.db import models
from .managers import CustomMovieManager


class Genre(models.Model):
    tmdb_id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Movie(models.Model):
    tmdb_id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=150)
    runtime = models.PositiveSmallIntegerField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField("Genre", related_name="movies")

    objects = CustomMovieManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title"]
