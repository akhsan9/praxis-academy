# Generated by Django 2.2 on 2020-11-09 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_barang_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='status',
        ),
    ]
