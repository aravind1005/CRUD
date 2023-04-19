from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

