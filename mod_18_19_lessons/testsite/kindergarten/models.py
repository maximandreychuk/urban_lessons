from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )  # выборка для статуса
    title = models.CharField(max_length=250)  # поле название поста
    # поле для ссылки на пост c уникальной датой
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')  # внешний ключ, наследованный от модели User, при удалении автора - удаляются все связанные с ним посты
    body = models.TextField()  # текст поста
    publish = models.DateTimeField(default=timezone.now)  # дата публикации
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    updated = models.DateTimeField(auto_now=True)  # дата апдэйта публикации
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')  # поле выбора статуса

    class Meta:
        ordering = ('-publish',)  # сортировка постов по дате публикации

    def __str__(self):
        return self.title  # при вызове поста будет возвращаться его title


"""Собственная модель."""

User = get_user_model()


class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
