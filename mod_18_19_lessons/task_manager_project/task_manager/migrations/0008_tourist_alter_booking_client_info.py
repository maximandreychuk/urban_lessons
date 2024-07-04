# Generated by Django 5.0.6 on 2024-06-26 08:50

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('task_manager', '0007_alter_booking_client_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='client_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_tourist', to='task_manager.tourist'),
        ),
    ]