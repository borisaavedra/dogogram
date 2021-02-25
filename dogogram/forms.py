from django import forms
from django.contrib.auth.models import User
from users.models import Profile
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    username = forms.CharField(
        label="",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
            "class": "form-control",
            "placeholder": "Username"
            })
    )

    password = forms.CharField(
        label="",
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Password"
            }
        )
    )

    pass_confirmation = forms.CharField( 
        label="",
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Password"
            }
        )
    )

    first_name = forms.CharField(
        label="",
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
            "class": "form-control",
            "placeholder": "First name"
            })
    )

    last_name = forms.CharField(
        label="",
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
            "class": "form-control",
            "placeholder": "Last name"
            })
    )

    email = forms.CharField(
        label="",
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
            "class": "form-control",
            "placeholder": "Email"
            })
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise ValidationError("User already taken")

        return username

    def clean(self):
        data = super().clean()

        password = data["password"]
        pass_confirmation = data["pass_confirmation"]

        if password != pass_confirmation:
            raise ValidationError("Password do not match")

        return data

    def save(self):
        data = self.cleaned_data
        data.pop("pass_confirmation")

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()