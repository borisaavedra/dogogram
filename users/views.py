# Users's views

# Django
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView, CreateView, DeleteView

# Dogogram
from posts.models import Post
from dogogram.forms import SignUpForm
from users.forms import FollowForm
from users.models import Profile, FollowingFollowers

# Create your views here.


class UnfollowView(LoginRequiredMixin, DeleteView):
    template_name =  "users/unfollow.html"
    model = FollowingFollowers
    form_class = FollowForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        follower_user_pk = self.request.POST["follower_user"]
        self.follower_user = User.objects.filter(pk=follower_user_pk).first()
        self.follower_username = self.follower_user.username

    def get_object(self):
        unfollow_obj = FollowingFollowers.objects.get(
            Q(following_user=self.request.user) & Q(follower_user=self.follower_user)
        )
        return unfollow_obj

    def get_success_url(self):
        username = self.follower_username
        return reverse('users:detail', kwargs={'username': username})


class FollowView(LoginRequiredMixin, CreateView):
    template_name = "users/follow.html"
    model = FollowingFollowers
    form_class = FollowForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        follower_user_pk = self.request.POST["follower_user"]
        follower_user = User.objects.filter(pk=follower_user_pk).first()
        self.follower_username = follower_user.username

    def get_success_url(self):
        username = self.follower_username
        return reverse('users:detail', kwargs={'username': username})


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update.html'
    model = Profile
    fields = ['website', 'bio', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class UserDetailView(LoginRequiredMixin, DetailView):
    
    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by("-create_at")
        friend = FollowingFollowers.objects.filter(
            following_user=self.request.user
        ).filter(
            follower_user=context["user"]
        )
        if friend:
            context["is_friend"] = True
        return context


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):

    template_name = "users/login.html"
    redirect_authenticated_user = True # Evita que el usuario ya logado vuelva a la pagina de login


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass
    
    # next_page = reverse("users:login")


#########################################
# Esta es la function view para el log out
#########################################
# @login_required
# def dogo_logout(request):
#     logout(request)
#     return redirect("users:login")


#########################################
# Esta es la function view para el log in
#########################################
# def dogo_login(request):
    
#     if request.method == "POST":
        
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("posts:pretty_posts")
#         else:
#             return render(request, "users/login.html", {"error":"Invalid username or password"})
    
#     return render(request, "users/login.html")


#########################################
# Esta es la function view para sign up
#########################################
# def dogo_signup(request):

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect("users:signup")

#     else:
#         form = SignUpForm()

#     return render(request, "users/signup.html", { "form": form })


###################################
# Actualizar el perfil de usuario
# en Function View
###################################
# @login_required
# def dogo_update_profile(request):
#     profile = request.user.profile

#     if request.method == "POST":
#         form = UpdateForm(request.POST, request.FILES)

#         if form.is_valid():
#             data = form.cleaned_data
#             profile.website = data["website"]
#             profile.bio = data["bio"]
#             profile.picture = data["picture"]
#             profile.phone_number = data["phone_number"]
#             profile.save()
            
#             url = reverse("users:login")
#             redirect(url)
        
#     else:
#         form = UpdateForm()

#     return render(
#         request,
#         "users/update.html",
#         { 
#             "profile":profile,
#             "form":form,
#         })