from django.db import models

# Create your models here.

class BikeRacks(models.Model):
    address = models.CharField(max_length=50, default="", unique=True)
    rating = models.IntegerField(default="", unique=False)
    school = models.CharField(max_length=50, default='', unique=False)
    players = models.CharField(max_length=50, default='', unique=False)

    def __str__(self) -> str:
        return self.address