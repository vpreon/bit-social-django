from django.db import models

from core.models import AppBaseModel


class Post(AppBaseModel):
    text = models.CharField(max_length=500)
