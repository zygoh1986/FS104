# views.py
from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import TodolistSerializer
from .models import Hero
from .models import Todolist

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.all().order_by('tasks')
    serializer_class = TodolistSerializer
