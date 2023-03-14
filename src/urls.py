from django.urls import path

from src.views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]
