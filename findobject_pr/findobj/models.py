from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='findobj/media/loads')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_images', default=1)
    confidence = models.CharField(max_length=10, default='0%')
