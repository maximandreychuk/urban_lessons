from django.urls import path
from . import views


app_name = 'task_manager'
urlpatterns = [
    path('', views.get_tasks, name='tasks_list'),
    path('<int:task_id>/', views.get_task, name='task_detail'),
    path('five_comments/', views.get_five_comments, name='five_commetns'),
    path('add_comment/<int:task_id>/', views.add_comment, name='user_info'),

    # далее - Домашнее задание по теме "DTL. Подробнее о шаблонах и тегах.
    path('array/', views.array, name='array'),
    path('get_time/', views.different_time_formats,
         name='different_time_formats'),
    path('pages/', views.get_all_pages,
         name='all_pages'),
    path('pages/<slug:page_slug>/', views.get_page_detail,
         name='page_detail'),
    path('generate_tag/', views.random_tag_color,
         name='tags_color'),
]
