from django.urls import path
from . import views


app_name = 'booking'
urlpatterns = [
    path('register/', views.register),
    path('booking/', views.booking),
]
