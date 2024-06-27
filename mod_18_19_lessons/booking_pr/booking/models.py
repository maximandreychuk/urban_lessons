from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Tourist(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=11, default='89153276063')
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField(default='1')

    def __str__(self):
        return self.first_name


class Tour(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Название: {self.name}, даты проведения: {self.start_date} - {self.end_date}'


class ExtraService(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    PAY_CHOICES = (
        ('cash', 'Наличными'),
        ('card', 'Картой'),
        ('sbp', 'СБП'),
    )
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='booking_tour')
    start_date = models.DateField(default='2024-03-10')
    end_date = models.DateField(default='2024-02-10')
    adults = models.IntegerField()
    children = models.IntegerField(default=0)
    extraservice = models.ForeignKey(
        ExtraService, on_delete=models.CASCADE, related_name='booking_extraservice', null=True,
        blank=True)
    pay_method = models.CharField(
        max_length=20, choices=PAY_CHOICES, default='cash')
    tourist = models.ForeignKey(
        Tourist, on_delete=models.CASCADE, default="", related_name='booking_tourist', null=True,
        blank=True)
