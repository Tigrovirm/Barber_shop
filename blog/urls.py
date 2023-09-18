from django.urls import path
from .views import ListReviews, CreateReview, HomeView, ListPosts, MakeAppointment

app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/", ListPosts.as_view(), name="blog"),
    path("reviews/", ListReviews.as_view(), name="list_reviews"),
    path("create_review/", CreateReview.as_view(), name="create_review"),
    path("make_appointment/", MakeAppointment.as_view(), name="make_appointment"),
]
