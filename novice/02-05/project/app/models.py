from django.db import models
from datetime import datetime


# Create your models here.
class Task(models.Model):
    name = models.CharField(default='nama', max_length=255)
    telp = models.IntegerField(null=True)
    seri = models.CharField(default='seri', max_length=255)
    status = models.CharField(default='pending', max_length=255)
