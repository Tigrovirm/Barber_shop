from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin



class RegisterUser(CreateView):
    model = User
    fields = '__all__'
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:home")

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "staffonly/profile.html"

class ListPost(LoginRequiredMixin, ListView):
    queryset = posts = Post.objects.filter(publish=False)
    context_object_name = "posts"
    template_name = "staffonly/list_posts.html"

class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "staffonly/detail_post.html"
    context_object_name = "post"


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "staffonly/create_post.html"
    success_url = reverse_lazy("staffonly:list_posts")


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "staffonly/edit_post.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("staffonly:list_posts")


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "staffonly/delete_post.html"
    context_object_name = "post"
    success_url = reverse_lazy("staffonly:list_posts")

class ProfileReviews(LoginRequiredMixin, TemplateView):
    template_name = "staffonly/profile_reviews.html"

