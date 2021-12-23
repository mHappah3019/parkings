from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BikeRacksSerializer
from .models import BikeRacks

# Create your views here.    

class BikeRacksView(generics.ListAPIView):
    queryset = BikeRacks.objects.all()
    serializer_class = BikeRacksSerializer


class BikeRacksADDView(generics.CreateAPIView):
    queryset = BikeRacks.objects.all()
    serializer_class = BikeRacksSerializer