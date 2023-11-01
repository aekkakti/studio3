from django.apps import AppConfig
from django.db import models

class MainConfig(AppConfig):
   verbose_name = 'Дизайнерский сайт'
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'designstudio'
