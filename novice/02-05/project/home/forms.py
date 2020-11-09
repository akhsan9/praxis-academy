from django.forms import ModelForm

from . import models

class HomeForm(ModelForm):
    class Meta :
        model = models.Homer
        exclude=[]