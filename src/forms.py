from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList

from src.models import Task


class CustomErrorList(ErrorList):
    def get_context(self):
        return {
            "errors": self,
            "error_class": "alert alert-danger h6 list-unstyled",
        }


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    error_messages = {
        "password_mismatch": "Пароли не совпадают"
    }
    attrs = {"class": "form-control h6"}
    username = forms.CharField(label='Имя пользвателя', widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs=attrs))
    email = forms.EmailField(label='Ваша почта', widget=forms.EmailInput(attrs=attrs))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    username_label = "Имя пользвателя"
    passwors_label = "Пароль"
    username_attrs = {"class": "form-control", "placeholder": username_label}
    password_attrs = {"class": "form-control mt-3", "placeholder": passwors_label}
    username = forms.CharField(label='', widget=forms.TextInput(attrs=username_attrs))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs=password_attrs))
    error_messages = {
        "invalid_login": (
            "Вы ошиблись паролем, логином, или у вас еще не создан аккаунт."
            " Поля чувствительны к регистру будьте осторожнее."
        ),
        "inactive": "Аккаунт был забанен",
    }


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'category']
