from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<id>/view-home', views.detaile),
    path('<id>/edit-home', views.edited),
    path('<id>/hapus-home', views.delete),
]
