from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<id>/', views.detil),
    path('<id>/edit', views.edit),
    path('<id>/hapus', views.delete),
]
