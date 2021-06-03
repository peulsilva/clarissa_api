from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlantaSerializer
from .models import Planta
# Create your views here.

class PlantaViewset(viewsets.ModelViewSet):
    serializer_class = PlantaSerializer
    queryset = Planta.objects.all()



