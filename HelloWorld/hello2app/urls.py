# hello2app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
]
