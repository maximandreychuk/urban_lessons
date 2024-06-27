from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import BookingForm, RegistrationForm, TouristForm
from django.core.exceptions import ValidationError
# from .models import Tour


def validate_data(email, password):
    if '@' not in email:
        return f'Неверный формат email {email}'
    elif len(password) < 8:
        return f'Пароль {password} слишком короткий'
    else:
        return 'Данные прошли валидацию'


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return HttpResponse(f'<h2>Hello, {username}</h2>')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        tourist_form = TouristForm(request.POST)
        if booking_form.is_valid() and tourist_form.is_valid():
            booking_form.save()
            tourist_form.save()
            return HttpResponse(f'<h2>Бронь прошла успешно, {tourist_form.cleaned_data.get('first_name')}!</h2>')
    else:
        booking_form = BookingForm()
        tourist_form = TouristForm()
    return render(request,
                  'booking.html',
                  {'booking_form': booking_form,
                   'tourist_form': tourist_form}
                  )
