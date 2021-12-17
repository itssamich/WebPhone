from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

    username = models.CharField(max_length=16, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=100, default='')

class Post(models.Model):
    def __str__(self):
        return str(self.id)

    body = models.TextField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)