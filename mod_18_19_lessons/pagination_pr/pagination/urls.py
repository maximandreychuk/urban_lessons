from django.urls import path
from . import views


app_name = 'pagination'
urlpatterns = [
    path('posts/', views.get_posts),
]
