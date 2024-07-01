from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, 'base.html')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('base')


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('base')


def logout_user(request):
    logout(request)
    return redirect('login')
