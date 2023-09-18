from django.urls import path, include
from .views import RegisterUser, ProfileView, ListPost, CreatePost, DetailPost, DeletePost, EditPost, ProfileReviews



app_name = "staffonly"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path("", ProfileView.as_view(), name="profile"),
    path("create_post/", CreatePost.as_view(), name="create_post"),
    path("list_posts/", ListPost.as_view(), name="list_posts"),
    path("list_posts/<int:pk>/", DetailPost.as_view(), name="detail_post"),
    path("edit_post/<int:pk>/", EditPost.as_view(), name="edit_post"),
    path("list_posts/<int:pk>/delete/", DeletePost.as_view(), name="delete_post"),
    path("profile_reviews/", ProfileReviews.as_view(), name="profile_reviews"),
]