from rest_framework import serializers

from .models import BikeRacks


class BikeRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeRacks
        fields = ('id', 'address', 'rating', 'school', 'players', 'surveillance_efficiency')