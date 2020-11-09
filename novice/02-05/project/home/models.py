from django.db import models

# Create your models here.
class Homer(models.Model):
    nama = models.CharField(default='nama', max_length=255)
    telpon = models.CharField(default='', max_length=15)
    kota = models.CharField(default='jogja', max_length=30)
    statuses = models.CharField(default='Ready', max_length=255)

    def __str__(self):
        return self.nama
