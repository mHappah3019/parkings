from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import BikeRacks
from .serializers import BikeRacksSerializer

# Create your views here.    

class BikeRacksView(generics.ListAPIView):
    queryset = BikeRacks.objects.all()
    serializer_class = BikeRacksSerializer


class BikeRacksADDView(generics.CreateAPIView):
    queryset = BikeRacks.objects.all()
    serializer_class = BikeRacksSerializer