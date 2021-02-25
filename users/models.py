# Users models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # para que herede del model User de Django

    website = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class FollowingFollowers(models.Model):
    
    following_user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE, null=True)

    follower_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.following_user} follows {self.follower_user}"

