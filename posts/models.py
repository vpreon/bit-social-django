from django.db import models

from accounts.models import User
from core.models import AppBaseModel


class Post(AppBaseModel):
    text = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('self', on_delete=models.CASCADE, related_name='post_share', blank=True, null=True)




class PostReact(AppBaseModel):
    class Reacts(models.TextChoices):
        like = "LIKE"
        dislike = "DISLIKE"

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_react')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    react = models.CharField(max_length=50, choices=Reacts)
    
    class Meta:
        unique_together = ("post", "user")


class PostComment(AppBaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)


class PostView(AppBaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_view')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Media(AppBaseModel):
    image = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='medias')