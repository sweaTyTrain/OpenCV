from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('webcam/', views.webcam, name='webcam'),
]