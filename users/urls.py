# User's urls

from django.urls import path
from users import views

urlpatterns = [

    path(
        route="login/", 
        view=views.LoginView.as_view(),
        name="login"
    ),

    path(
        route="logout",
        view=views.LogoutView.as_view(),
        name="logout"),

    path(
        route="signup",
        view=views.SignUpView.as_view(),
        name="signup"),

    path(
        route="me/profile",
        view=views.UpdateProfileView.as_view(),
        name="update"),

    path(
        route="follow/",
        view=views.FollowView.as_view(),
        name="follow"),

    path(
        route="unfollow/",
        view=views.UnfollowView.as_view(),
        name="unfollow"),

    path(
        route="<str:username>/",
        view=views.UserDetailView.as_view(),
        # view=TemplateView.as_view(template_name="users/detail.html"), # Una clase solo para mostrar un template
        name="detail"
    ),

]