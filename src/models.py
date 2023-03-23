from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=127)
    importance = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return f"{self.name}, рейтинг важности:{self.importance}"

    class Meta:
        ordering = ['importance']


class Task(models.Model):
    name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Название:{self.name}, категория:{self.category.name}, пользватель:{str(self.user)}"

    class Meta:
        ordering = ['created_at']
