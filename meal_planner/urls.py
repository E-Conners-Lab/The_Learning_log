"""Defines URL patterns for meal_planner"""

from django.urls import path

from . import views

app_name = 'meal_planner'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]