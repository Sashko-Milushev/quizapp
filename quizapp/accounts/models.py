from django.db import models
from django.contrib.auth import models as auth_models

from quizapp.accounts.managers import QuizUserManager


class QuizUser(auth_models.AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    username = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False

    )

    objects = QuizUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']
