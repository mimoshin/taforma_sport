from django.urls import path
from .views import *


"""Metodos públicos sin autenticación"""
publicpatterns = [
    path('', BaseView, name='principal'),
    path('calendar/', CalendarView, name='calendar'),
    path('calendar/month/', CalendarViewMonth, name='calendar_month'),
    path('championships/', ChampionshipsView, name='championships'),
    path('championships/<slug:slug>/', ChampionshipDetailView, name='championship_detail'),
]

urlpatterns = publicpatterns
