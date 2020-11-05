# from django.shortcuts import render

# from . import models

# Create your views here.

#	Cara menambahkan data atau 'CREATE' data
# def index(req): # definisikan method index, parameter request
# 		tasks = models.Task.objects.all() # ditampung di Variabel tasks
# 	return render(req, 'home/index.html', {
#          'data': tasks, 
# 		})  

from django.shortcuts import render

def index(req):
    return render(req, 'home/index.html')
