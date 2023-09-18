from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200, blank=False)
    content = models.TextField(verbose_name="Контент", blank=False)
    publish = models.BooleanField(verbose_name="Состояние", default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Master(AbstractBaseUser):
    email = models.CharField(verbose_name="Email", max_length=10, blank=False, default="None")
    phone = models.CharField(verbose_name="Телефон", max_length=10, blank=False, default="None")
    first_name = models.CharField(verbose_name="Имя", max_length=10, blank=False, default="None")
    last_name = models.CharField(verbose_name="Фамилия", max_length=10, blank=False, default="None")

   

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.first_name
