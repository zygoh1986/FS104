# models.py
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Todolist(models.Model):
    tasks = models.CharField(max_length=60)
    priority = models.CharField(max_length=60)
    duedate = models.DateField()

    def __str__(self):
        return self.name