from django.db import models
from django.utils import timezone


class Engineer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Location(models.Model):
    distance_km = models.IntegerField()
    name = models.CharField(max_length=255)


class Visits(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    date = models.DateTimeField(default=timezone.now)
