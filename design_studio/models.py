from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class MainConfig(AppConfig):
   verbose_name = 'Дизайнерский сайт'
   name = 'design_studio'

class AdvUser(AbstractUser):
   name = models.CharField(max_length=250, verbose_name="ФИО", help_text="Только кириллические буквы, дефис и пробелы")
   username = models.CharField(max_length=35, verbose_name="Логин", unique=True, help_text="Только латиница и дефис, уникальный")
   is_activated = models.BooleanField(default=True, db_index=True,
                                      verbose_name='Согласен с обработкой '
                                                   'персональных данных?')

class Meta(AbstractUser.Meta):
   pass


class Request(models.Model):
    request_name = models.CharField(max_length=254, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    photo_of_room = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.request_name
