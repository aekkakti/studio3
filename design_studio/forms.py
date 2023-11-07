import re
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ('name', 'username', 'email', 'password1', 'password2', 'is_activated')

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[а-яА-Я\s-]+$', name):
            raise ValidationError("ФИО может содержать только кириллицу, дефис и пробелы. ")
        return name

    def clean_login(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z\s-]+$', username):
            raise ValidationError("Логин может содержать только латиницу и дефис. ")
        if AdvUser.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким логином уже существует. ")
        return username

class CreateRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('request_name', 'description', 'category', 'photo_of_room')

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class RequestUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('status', 'comment', 'new_design')

    def clean(self):
        super().clean()
        status = self.cleaned_data.get('status')
        new_design = self.cleaned_data.get('new_design')
        comment = self.cleaned_data.get('comment')

        if status == 'd' and not new_design:
            raise ValidationError('Меняя статус заявки на "Выполнено", прикрепите изображение')
        elif status == 'd' and comment:
            raise ValidationError('Указывая статус "Выполнено", вы не должны указывать комментарий')

        if status == 'a' and not comment:
            raise ValidationError('Меняя статус заявки на "Принято в работу", укажите комментарий')
        elif status == 'a' and new_design:
            raise ValidationError(
                'Меняя статус заявки на "Принято в работу, вы не можете прикрепить изображение')



