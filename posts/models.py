from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.utils.html import mark_safe

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/picture")

    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    likes = models.IntegerField(default=0)

    @property
    def thumbnail_preview(self):
        if self.photo:
            return mark_safe(f"<img src='{self.photo.url}' width='300px' height='300px'>")
        return ""

    def __str__(self):
        return f"{self.title} by {self.user.username}"
