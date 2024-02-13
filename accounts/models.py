from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager
from core.models import AppBaseModel


class User(AbstractUser, AppBaseModel):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(blank=True, null=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
