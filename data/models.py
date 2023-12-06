from django.db import models
from django.utils import timezone


class Engineer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    distance_km = models.IntegerField()
    name = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_distance_another_location(self, location):
        difference = self.distance_km - location.distance_km
        return abs(difference)

    def display_distance_with_name(self, location):
        distance_client_location = self.get_distance_another_location(location)
        return f"{distance_client_location}km away"


class LocationEngineer(Location):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)


class LocationClient(Location):
    pass
