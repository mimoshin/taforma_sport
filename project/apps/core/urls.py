from django.urls import path
from .views import *


"""Metodos públicos sin autenticación"""
publicpatterns = [
    path('', BaseView, name='principal'),
    path('calendar/', CalendarView, name='calendar'),
    path('calendar/month/', CalendarViewMonth, name='calendar_month'),
    path('championships/', ChampionshipsView, name='championships'),
    path('championships/<slug:slug>/', ChampionshipScheduleView, name='championship_detail'),
    path('championships/<slug:slug>/resultados/', ChampionshipDetailView, name='championship_results'),
    path('championships/<slug:slug>/resultados/<slug:event_slug>/', ChampionshipEventResultsView, name='championship_event_results'),
    path('championships/<slug:slug>/puntajes/', ChampionshipScoresView, name='championship_scores'),
    path('ranking/', RankingView, name='ranking'),
    path('login/', LoginPageView, name='login'),
    path('registro/', RegisterPageView, name='register'),
]

urlpatterns = publicpatterns
