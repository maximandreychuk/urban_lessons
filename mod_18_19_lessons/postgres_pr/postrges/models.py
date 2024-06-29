from django.db import models


class User(models.Model):
    user = models.CharField(unique=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=11, default='89153276063')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.user
