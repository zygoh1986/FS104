from rest_framework import viewsets

from .models import HelloWorld


class HelloWorldViewSet(viewsets.ModelViewSet):
    queryset = HelloWorld.objects.all().order_by('name')
    serializer_class = HelloWorldSerializer
