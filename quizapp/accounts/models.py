from django.db import models
from django.contrib.auth import models as auth_models

from quizapp.accounts.managers import QuizUserManager


class QuizUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
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

    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    is_deleted = models.BooleanField(
        default=False,
        blank=False,
        null=False
    )
    objects = QuizUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class RevokedToken(models.Model):
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['token']
