from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<id>/view-barang', views.detil),
    path('<id>/edit-barang', views.edit),
    path('<id>/hapus-barang', views.delete),
]
