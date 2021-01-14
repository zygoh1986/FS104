# serializers.py
from rest_framework import serializers

from .models import HelloWorld

class HelloWorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelloWorld
        fields = ('name')