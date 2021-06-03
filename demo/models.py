from django.db import models
from datetime import datetime



# Create your models here.
class Planta(models.Model):
    name=models.CharField(max_length=300, unique=True, blank=False)
    species=models.CharField(max_length=300,blank=False, unique=False)
    date=models.DateField(default=datetime.date(datetime.today()))
    image=models.FileField(upload_to='Images', blank=True)