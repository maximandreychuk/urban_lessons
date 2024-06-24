from django.db import models
from django.urls import reverse
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


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_comments')
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_comments')
    created = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=True)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)


class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/pages/{self.slug}'


# далее - Домашнее задание по теме "Модели"
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author_books')


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    books = models.ManyToManyField(Book, through='PublisherBook')


class PublisherBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


# 5) Реализуйте ER модель базы данных склада в любом удобном вам редакторе(не менее 7 сущностей)

class Warehouse(models.Model):
    title = models.CharField(max_length=100)
    goods_category = models.CharField(max_length=100)


class Manager(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='manager_warehouses')


class TechicalMachine(models.Model):
    use = models.CharField(max_length=100)
    title = models.CharField(max_length=100)


class Loader(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='loader_warehouses')
    techical_machine = models.ForeignKey(
        TechicalMachine, on_delete=models.CASCADE, related_name='loader_technical_machines')


class Shipper(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()


class Goods(models.Model):
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    shipper = models.ForeignKey(
        Shipper, on_delete=models.CASCADE, related_name='goods_shipper')
    warehouse = models.ManyToManyField(Warehouse, through='GoodsWarehouse')


class Stocktaking(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='stocktaking_warehouses')
    date = models.DateField()
    difference = models.IntegerField()
    done = models.BooleanField()


class GoodsWarehouse(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
