from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from rest_framework.authtoken.models import Token


# Create your models here.

class Task(models.Model):
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    desc = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    taskDueDate = models.DateField()

    def __str__(self):
        return self.title
