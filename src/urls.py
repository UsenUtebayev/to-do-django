from django.urls import path

from src.views import add_task, delete_task, change_password, get_task_detail
from src.views import index, register, login_user, logout_user, edit_task, add_task_category

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-task/', add_task, name='add-task'),
    path('add-task-category/', add_task_category, name='add-task-category'),
    path('delete-task/<pk>', delete_task, name='delete-task'),
    path('change-password', change_password, name='change-password'),
    path('<int:pk>/', get_task_detail, name='task-detail'),
    path('edit/<int:pk>', edit_task, name='edit-task')
]
