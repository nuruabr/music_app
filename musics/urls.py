from django import views
from django.urls import path
from . import views
urlpatterns = [
    path("", views.all_data, name="home_data")
]
