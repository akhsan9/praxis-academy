from django.forms import ModelForm

from . import models

class BarangForm(ModelForm):
    class Meta :
        model = models.Barang
        exclude=[]