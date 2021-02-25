
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostFeedView.as_view(), name="pretty_posts"),

    path(
        route="posts/new/", 
        view=views.CreatePostView.as_view(),
        name="new_post"),
    
    path(
        route="posts/like/<int:pk>/",
        view=views.PostUpdateView.as_view(),
        name="like"),

    path(
        route="posts/<int:pk>",
        view=views.PostDetailView.as_view(),
        name="detail"),

]