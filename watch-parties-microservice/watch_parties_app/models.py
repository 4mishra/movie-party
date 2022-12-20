from django.db import models
from django.core.validators import MinLengthValidator


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
