from django.shortcuts import render
from django.views.generic import ListView, CreateView, ListView, TemplateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Service
from blog.models import Appointment


class ServicesView(LoginRequiredMixin, TemplateView):
    template_name = "services/title_services.html"

class ListService(LoginRequiredMixin, ListView):
    queryset = services = Service.objects.filter(publish=False)
    context_object_name = "services"
    template_name = "services/list_services.html"

class CreateService(LoginRequiredMixin, CreateView):
    model = Service
    fields = ["title", "price"]
    template_name = "services/create_services.html"
    success_url = reverse_lazy("services:list_services")

class ListAppointment(LoginRequiredMixin, ListView):
    queryset = appointments = Appointment.objects.filter(publish=False)
    context_object_name = "appointments"
    template_name = "services/list_appointment.html"

class EditAppointment(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = "services/edit_appointment.html"
    fields = ['service', 'master','appointment_date', 'appointment_time']
    success_url = reverse_lazy("services:list_appointment")

class DetailAppointment(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = "services/detail_appointment.html"
    context_object_name = "appointment"

class DeleteAppointment(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = "services/delete_appointment.html"
    context_object_name = "appointment"
    success_url = reverse_lazy("services:list_appointment")