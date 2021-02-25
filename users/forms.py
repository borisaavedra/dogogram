# Users Forms

from django.forms import ModelForm
from users.models import FollowingFollowers

class FollowForm(ModelForm):
    class Meta:
        model = FollowingFollowers
        fields = ["following_user", "follower_user"]

