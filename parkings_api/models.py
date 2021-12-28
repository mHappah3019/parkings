from django.db import models

# Create your models here.

COLOR_CHOICES = [
    ("GREEN", "GREEN"),
    ("RED", "RED"),
    ("YELLOW", "YELLOW"),
]

class BikeRack(models.Model):
    address = models.CharField(max_length=50, default="", unique=True)
    rating = models.IntegerField(default="", unique=False)
    school = models.CharField(max_length=50, default='', unique=False)
    players = models.CharField(max_length=50, default='', unique=False)
    surveillance_efficiency = models.CharField(max_length=50, choices=COLOR_CHOICES, default="RED")

    def __str__(self) -> str:
        return self.address