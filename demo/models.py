from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
class Planta(models.Model):
    name=models.CharField(max_length=300, unique=True, blank=False)
    species=models.CharField(max_length=300,blank=False, unique=False)
    date=models.DateField(default=datetime.date(datetime.today()))
    image=models.FileField(upload_to='Images', default='planta.png', blank=True, null=True)


