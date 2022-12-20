from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.core.validators import MinLengthValidator, EmailValidator


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False,
        validators=[MinLengthValidator(5), EmailValidator()],
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.username
