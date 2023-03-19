from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from src.forms import *
from src.models import *


# Create your views here.
def index(request):
    tasks = Task.objects.filter(user=request.user.pk).exclude(disabled=1)
    cats = Category.objects.all()
    context = {"title": "Главная!", "cats": cats, 'tasks': tasks}
    return render(request, 'index.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистраций')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {"form": form, "title": "Регистрация!"})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm
    return render(request, 'login.html', {'form': form, "title": "Вход!"})


def logout_user(request):
    logout(request)
    return redirect('login')


def add_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskCreationForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, "Задача добавлена успешно!")
                return redirect('add-task')
        else:
            messages.error(request, 'Что то пошло не так')
        form = TaskCreationForm()
        return render(request, 'add-task.html', {"form": form, "title": "Добавить задачу"})
    return redirect('index')


def delete_task(request, pk):
    if request.user.pk != Task.objects.get(pk=pk).user_id:
        raise PermissionDenied("Вы не можете удалять чужие таски")
    Task.objects.filter(pk=pk).update(disabled=1)
    return redirect('index')
