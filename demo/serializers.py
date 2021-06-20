from rest_framework import serializers
from .models import Planta, BD

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields='__all__'

class BDSerializer(serializers.ModelSerializer):
    class Meta:
        model= BD
        fields='__all__'





