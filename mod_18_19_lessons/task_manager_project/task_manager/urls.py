from django.urls import path
from . import views


app_name = 'task_manager'
urlpatterns = [
    path('', views.get_tasks, name='tasks_list'),
    path('<int:task_id>/', views.get_task, name='task_detail'),
    path('five_comments/', views.get_five_comments, name='five_commetns'),
    path('add_comment/<int:task_id>/', views.add_comment, name='user_info'),
]
