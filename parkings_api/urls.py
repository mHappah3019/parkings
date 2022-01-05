from django.conf.urls import include
from django.urls import path

from .views import BikeRacksADDView, BikeRacksView

urlpatterns = [
    path('get-data/', BikeRacksView.as_view())
]