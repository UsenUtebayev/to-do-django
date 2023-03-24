from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from src.forms import UserRegistrationForm, UserLoginForm, TaskCreationForm, ChangePasswordForm
from src.models import Task, Category


# Create your views here.
def index(request):
    context = {"title": "Главная!"}
    if request.user.is_authenticated:
        categories = Category.objects.all()
        context_tasks = {}
        for cat in categories:
            context_tasks.update({cat: Task.objects.filter(category=cat.pk, user=request.user.pk, disabled=False)
                                 .select_related('category', 'user')})
        context.update({"cats": categories, 'tasks': context_tasks})
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
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Задача добавлена успешно!")
            return redirect('index')
    else:
        messages.error(request, 'Не получилось добавть задачу')
    form = TaskCreationForm()
    return render(request, 'add-task.html', {"form": form, "title": "Добавить задачу"})


def delete_task(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if instance.user.pk != request.user.pk:
        raise PermissionDenied('Вы не можете удалять чужие таски')
    instance.disabled = True
    instance.save(update_fields=['disabled'])
    return redirect('index')


@login_required()
def change_password(request):
    form = ChangePasswordForm(data=request.POST, user=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('logout')

    return render(request, 'change-password.html', context={"form": form, "title": "Смена пароля"})


def get_task_detail(request, pk):
    task_item = get_object_or_404(Task.objects.filter(disabled=False), pk=pk)
    if task_item.user.pk == request.user.pk:
        return render(request, 'task-detail.html', context={"task_item": task_item})
    raise PermissionDenied("Вы не можете просматривать чужие таски")


@login_required
def edit_task(request, pk):
    if pk:
        task = get_object_or_404(Task, pk=pk)
        if task.user != request.user:
            return HttpResponseForbidden()
    else:
        task = Task(user=request.user)

    form = TaskCreationForm(request.POST or None, instance=task)
    if request.POST and form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form, "title": "Редактировать задачу"}
    return render(request, 'edit-task.html', context)
