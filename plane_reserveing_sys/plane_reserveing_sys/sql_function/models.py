
# Create your models here.
from django.db import models

class Traveler(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    work_unit = models.CharField(max_length=200)
    id_number = models.CharField(max_length=20)
    travel_date = models.DateField()
    destination = models.CharField(max_length=200)
    file = models.FileField(upload_to='travel_files/', blank=True, null=True)