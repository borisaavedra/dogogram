# Posts's views

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from posts.form import PostsForm
from posts.models import Post
from users.models import FollowingFollowers
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator

# Create your views here.


class PostUpdateView(LoginRequiredMixin, UpdateView):

    queryset = Post.objects.all()
    fields = ["likes"]

    def get_object(self):
        obj = super().get_object()
        obj.likes += 1
        obj.save()
        return obj

    def render_to_response(self, context, **response_kwargs):
        return redirect(reverse("posts:pretty_posts")) # Redirije a la class view de para evitar la url


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    form_class = PostsForm
    success_url = reverse_lazy("posts:new_post")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile

        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    queryset = Post.objects.all()
    context_object_name = "post"


class PostFeedView(LoginRequiredMixin, ListView):
    template_name = "posts/feed.html"
    model = Post
    paginate_by = 30
    context_object_name = "posts"

    def get_queryset(self):
        followers_list = FollowingFollowers.objects.filter(
            following_user=self.request.user)
        posts_lists = Post.objects.filter(user__in=[ u.follower_user for u in followers_list ]).order_by("-create_at")
        return posts_lists


########################################
# Esta es la versión View Function-base
#@@#####################################
# @login_required
# def prettier_post(request):
#     posts = Post.objects.all().order_by("-create_at")

#     return render(request, "posts/feed.html", {"posts":posts})


#####################################
# Esta es la creación de un post con 
# function view based
######################################
# @login_required
# def new_post(request):
#     if request.method == "POST":
#         form = PostsForm(request.POST, request.FILES)

#         if form.is_valid:
#             form.save()
#             return render(
#                 request,
#                 "posts/new.html",
#                 {
#                     "form": form,
#                     "user": request.user,
#                     "profile": request.user.profile,
#                     "is_valid": form.is_valid,
#                 }
#             )

#     else:
#         form = PostsForm()
    
#     return render(
#         request,
#         "posts/new.html",
#         {
#             "form": form,
#             "user": request.user,
#             "profile": request.user.profile,
#             "is_valid": form.is_valid,
#         }
#     )