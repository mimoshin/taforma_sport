from django.urls import path
from .views import *


"""Metodos públicos sin autenticación"""
publicpatterns = [
    path('', BaseView, name='principal'),
]

urlpatterns = publicpatterns
