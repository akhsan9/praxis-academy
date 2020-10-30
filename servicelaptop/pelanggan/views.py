from django.shortcuts import render

from barang import models as barang_models
# Create your views here.
def index(req):
  barangs = barang_models.Barang.objects.all()
  return render(req, 'katalog/index.html', {
    'data': barangs,
  })