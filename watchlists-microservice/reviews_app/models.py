from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserReview(models.Model):
    movie = models.ForeignKey(
        "movies_app.Movie",
        related_name="user_reviews",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        "watchlists_app.UserVO",
        related_name="reviews",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.title}: {self.movie.title} reviewed by {self.user.username}"


class UserRating(models.Model):
    movie = models.ForeignKey(
        "movies_app.Movie",
        related_name="user_ratings",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        "watchlists_app.UserVO",
        related_name="ratings",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    score = models.SmallIntegerField(
        null=False,
        blank=False,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ],
    )
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.score}/10 for {self.movie.title} by {self.user.username}"
