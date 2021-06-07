from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlantaSerializer
from .models import Planta
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render
# Create your views here.

def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper


# @superuser_required()
class PlantaViewset(viewsets.ModelViewSet):
    # login_url = '/accounts/login'
    serializer_class = PlantaSerializer
    queryset = Planta.objects.all()








