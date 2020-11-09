from django.db import models

# Create your models here.
class Barang(models.Model):
    names = models.CharField(default='names', max_length=255)
    series = models.CharField(default='', max_length=15)
    stok = models.CharField(default='10', max_length=30)
    # status = models.CharField(default='Ready', max_length=255)
    
    def __str__(self):
        return self.names
