from django.urls import path
from . import views


app_name = 'task_manager'
urlpatterns = [
    path('', views.get_tasks, name='tasks_list')
]
