from django.contrib import admin

from src.models import *


# Register your models here.
@admin.register(Task)
@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass
