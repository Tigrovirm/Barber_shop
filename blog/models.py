from django.db import models
from django.utils import timezone
from staffonly.models import Master
from services.models import Service

class Review(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя", blank=False)
    phone = models.CharField(max_length=10, verbose_name="Номер телефона", blank=False)
    content = models.TextField(max_length=100, verbose_name="Отзыв", blank=False)
    publish = models.BooleanField(verbose_name="Состояние", default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(verbose_name="Оценка", default=5, blank=False)
    master = models.ForeignKey(Master, verbose_name="Мастер", on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return f"{self.grade}"


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    appointment_date = models.DateField(verbose_name="Дата записи", default=timezone.now)
    appointment_time = models.TimeField(verbose_name="Дата и время записи", default='09:00')
    publish = models.BooleanField(verbose_name="Состояние", default=False)
    is_booked = models.BooleanField(verbose_name="Забронировано", default=False)

    def __str__(self):
        return f"{self.service} - {self.appointment_time}"