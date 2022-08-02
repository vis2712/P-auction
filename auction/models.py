from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100,default='India')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Profile/', blank=True)

    def __str__(self):
        return f"{self.username}"
