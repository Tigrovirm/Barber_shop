from django.urls import path, include

from .views import ListService, CreateService, ListAppointment, ServicesView, DetailAppointment, EditAppointment, DeleteAppointment

app_name = "services"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("", ServicesView.as_view(), name="title_services"),
    path("list_services/", ListService.as_view(), name="list_services"),
    path("create_services/", CreateService.as_view(), name="create_services"),
    path("list_appointment/", ListAppointment.as_view(), name="list_appointment"),
    path("list_appointment/<int:pk>/", DetailAppointment.as_view(), name="detail_appointment"),
    path("edit_appointment/<int:pk>/", EditAppointment.as_view(), name="edit_appointment"),
    path("list_appointment/<int:pk>/delete/", DeleteAppointment.as_view(), name="delete_appointment"),
]