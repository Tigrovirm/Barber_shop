from .models import Review, Appointment
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, TemplateView, CreateView
from .forms import AppointmentForm


from datetime import datetime, date
from staffonly.models import Post, Master
from services.models import Service, Client

from telegram.management.commands import bot

# Create your views here.

class HomeView(TemplateView):
    template_name = "blog/home.html"

class ListReviews(ListView):
    queryset = Review.objects.filter(publish=True)
    context_object_name = "reviews"
    template_name = "blog/reviews.html"

class CreateReview(CreateView):
    model = Review
    fields = ["name", "phone", "content", "grade", "master"]
    template_name = "blog/create_review.html"
    success_url = reverse_lazy("blog:blog")


class ListPosts(ListView):
    queryset = Post.objects.filter(publish=True)
    context_object_name = "posts"
    template_name = "blog/blog.html"


class MakeAppointment(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "blog/make_appointment.html"
    success_url = reverse_lazy("blog:blog")
    uniq_id = 555655

    def send_telegram_message(self, uniq_id):
        client = Client.objects.get(uniq_id=uniq_id)
        bot.send_message(chat_id = client.telegram_id, text="Вы записались на стрижку")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = Master.objects.all()
        context['services'] = Service.objects.all()
        today = date.today()
        time_choices = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(9, 22) for minute in range(0, 60, 30)]
        context['time_choices'] = time_choices
        return context
    
    def form_valid(self, form):
        appointment_date = form.cleaned_data['appointment_date']
        appointment_time_str = form.cleaned_data['appointment_time']
        appointment_time = datetime.strptime(appointment_time_str, "%H:%M").time()
        selected_master_id = form.cleaned_data['master']

        appointment_datetime = datetime.combine(appointment_date, appointment_time)

        if appointment_datetime < datetime.now():
            error_message = 'Нельзя записаться на прошедшее время.'
            return self.render_to_response(self.get_context_data(form=form, error_message=error_message))

        if Appointment.objects.filter(appointment_date=appointment_date, appointment_time=appointment_time, master_id=selected_master_id).exists():
            error_message = 'Выбранное время уже занято.'
            return self.render_to_response(self.get_context_data(form=form, error_message=error_message))

        responce = super().form_valid(form)
        self.send_telegram_message(self.uniq_id)
        return responce





