from django.conf.urls import include
from django.urls import path

from .views import BikeRacksView, BikeRacksADDView

urlpatterns = [
    path('get-data/', BikeRacksView.as_view()),
    path('add-data/', BikeRacksADDView.as_view())
]