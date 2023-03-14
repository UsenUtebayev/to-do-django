from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from src.forms import *


# Create your views here.
def index(request):
    context = {}
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context.update({"username": username})
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
    return render(request, 'register.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
