# Generated by Django 5.0.6 on 2024-06-27 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField(default='1')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default='2024-03-10')),
                ('end_date', models.DateField(default='2024-02-10')),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('pay_method', models.CharField(choices=[('cash', 'Наличными'), ('card', 'Картой'), ('sbp', 'СБП')], default='cash', max_length=20)),
                ('extraservice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_extraservice', to='booking.extraservice')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_tour', to='booking.tour')),
                ('tourist', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_tourist', to='booking.tourist')),
            ],
        ),
    ]