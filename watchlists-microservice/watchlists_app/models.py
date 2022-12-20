from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)


class UserVO(models.Model):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[MinLengthValidator(1)],
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False,
        validators=[MinLengthValidator(5)],
    )

    def __str__(self):
        return self.username


class Watchlist(models.Model):
    owners = models.ManyToManyField("UserVO", related_name="watchlists")
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.owners:
            owners_str = " and ".join([owner.username for owner in self.owners.all()])
            return f"{self.name} by {owners_str}"
        else:
            return f"{self.name}"

    class Meta:
        ordering = ["date_updated"]


class WatchlistItem(models.Model):
    movie = models.ForeignKey(
        "movies_app.Movie", related_name="watchlist_items", on_delete=models.CASCADE
    )
    watchlist = models.ForeignKey(
        "Watchlist", related_name="watchlist_items", on_delete=models.CASCADE
    )
    watched = models.BooleanField(default=False)
    interest = models.PositiveSmallIntegerField(
        default=2,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3),
        ],
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.watchlist.name}: {self.movie.title}"

    class Meta:
        ordering = ["date_added"]
