# serializers.py
from rest_framework import serializers

from .models import Hero
from .models import Todolist

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias')


class TodolistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todolist
        fields = ('tasks', 'priority', 'duedate')