from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), #127.0.0.1:8000/home/
    path('create_region/', views.create_region, name='create_region'), #127.0.0.1:8000/create_region
]
