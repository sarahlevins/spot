from django.db import models
from users.models import CustomUser


class AnimalCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ColourCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CollarCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sighting(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField(null=True)
    description = models.TextField()
    species = models.CharField(null=True, max_length=50)
    image = models.ImageField(blank=True, null=True)
    animal_category = models.ForeignKey(
        AnimalCategory, on_delete=models.CASCADE, blank=True, null=True)
    colour_category = models.ForeignKey(
        ColourCategory, on_delete=models.CASCADE, blank=True, null=True)
    collar_category = models.ForeignKey(
        CollarCategory, on_delete=models.CASCADE, blank=True, null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Listing(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    animal_category = models.ForeignKey(
        AnimalCategory, on_delete=models.CASCADE, blank=True, null=True)
    colour_category = models.ForeignKey(
        ColourCategory, on_delete=models.CASCADE, blank=True, null=True)
    collar_category = models.ForeignKey(
        CollarCategory, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
