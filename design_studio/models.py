from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import django


class MainConfig(AppConfig):
    verbose_name = 'Дизайнерский сайт'
    name = 'design_studio'


class AdvUser(AbstractUser):
    name = models.CharField(max_length=250, verbose_name="ФИО", help_text="Только кириллические буквы, дефис и пробелы")
    username = models.CharField(max_length=35, verbose_name="Логин", unique=True,
                                help_text="Только латиница и дефис, уникальный")
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Согласен с обработкой '
                                                    'персональных данных?')


class Meta(AbstractUser.Meta):
    pass


class Request(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        max_size = 2.0
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Максимальный размер файла 2 МБ")

    request_name = models.CharField(max_length=254, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    REQUEST_STATUS = (
        ('n', 'Новая'),
        ('a', 'Принято в работу'),
        ('d', 'Выполнено'),
    )
    status = models.CharField(
        max_length=25,
        choices=REQUEST_STATUS,
        blank=True,
        default='n',
        verbose_name="Статус заявки")
    category = models.ForeignKey('category', on_delete=models.CASCADE, blank=True, verbose_name="Категория")
    photo_of_room = models.ImageField(max_length=254, upload_to="media/", verbose_name="Фотография",
                                      help_text="Разрешается формата файла только jpg, jpeg, png, bmp",
                                      validators=[
                                          FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
                                          validate_image])
    date = models.DateTimeField(default=django.utils.timezone.now)

    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    new_design = models.ImageField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'bmp']),
                                          validate_image], blank=True)
    comment = models.TextField(blank=True)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.request_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name