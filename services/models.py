from django.db import models
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=255)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    publish = models.BooleanField(verbose_name="Состояние", default=False)

    def __str__(self):
        return self.title
    

