# models.py
from django.db import models

class DataRecord(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.age} - {self.date}'

