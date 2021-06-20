from django import forms
from demo import models

class NovaPlanta(forms.ModelForm):
    class Meta:
        model=models.Planta
        fields=['name','species','date','image']

class RegarPlanta(forms.ModelForm):
    class Meta:
        model=models.Planta
        fields=['regada']