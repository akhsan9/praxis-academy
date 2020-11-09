from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    # path('<id>/', views.detaile),
    path('<id>/edit', views.edited),
    path('<id>/hapus', views.delete),
]
