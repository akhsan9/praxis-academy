# Generated by Django 2.2 on 2020-11-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='status',
            field=models.CharField(default='Ready', max_length=255),
        ),
    ]
