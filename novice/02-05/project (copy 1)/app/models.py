from django.db import models

# COLOR_CHOICES = (
#     ('jogja','JOGJA'),
#     ('sleman', 'SLEMAN'),
#     ('bantul','BANTUL'),
#     ('gunungkidul','GUNUNGKIDUL'),
#     ('kulonprogo','KULONPROGO'),
# )

# class Country(models.Model):
#     name = models.CharField(max_length=30, choices=COLOR_CHOICES)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# Create your models here.
class Task(models.Model):
    name = models.CharField(default='nama', max_length=255)
    telp = models.CharField(default='', max_length=15)
    seri = models.CharField(default='ASUS_', max_length=255)
    country = models.CharField(default='jogja', max_length=30)
    # country = models.ForeignKey(Country,choices=COLOR_CHOICES, on_delete=models.SET_NULL, null=True)
    kerusakan = models.TextField(default='')
    status = models.CharField(default='pending', max_length=255)

    def __str__(self):
        return self.name
