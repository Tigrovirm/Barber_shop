from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=255)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    publish = models.BooleanField(verbose_name="Состояние", default=False)

    def __str__(self):
        return self.title
    
class Client(models.Model):
    uniq_id = models.CharField(verbose_name="Уникальный ид", max_length=6, unique=True)
    telegram_id = models.CharField(verbose_name="Телеграм ИД", max_length=20, unique=True, blank=False)
    client_name = models.CharField(verbose_name="Имя клиента", max_length=14, unique=False, blank=False)
    phone = models.CharField(verbose_name="Телефон", max_length=10, unique=True, blank=False)
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.uniq_id}"
