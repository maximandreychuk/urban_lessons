from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Не начата'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_tasks')
    description = models.TextField()
    priority = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)],
        default=1)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='not_started')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-priority',)

    def __str__(self):
        return self.title
