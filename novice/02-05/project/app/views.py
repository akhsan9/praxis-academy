from django.shortcuts import render, redirect

from . import models

# Create your views here.

#	Cara menambahkan data atau 'CREATE' data
def index(req): # definisikan method index, parameter request
	if req.POST:
		models.Task.objects.create(name=req.POST['name'])
		return redirect('/') # mengembalikan (redirect) ke root /

	tasks = models.Task.objects.all() # ditampung di Variabel tasks
	return render(req, 'task/index.html', #mengembalikan (render) halaman yang mau ditampilkn
		{ 'data': tasks, # return dictionary untuk mengakses value di key, data menampung task, 
		}) 

#	Menghubungkan dengan halaman 'detail.html' membuat 'READ'
def detail(req, id):	
	task = models.Task.objects.filter(pk=id).first() # model first
	return render(req, 'task/detail.html',
		{ 'data': task,
		}) 

#	Membuat 'Edit'

def edit(req, id):
	if req.POST:
		models.Task.objects.filter(pk=id).update(
			name=req.POST['name'])
		return redirect('/')

	tasks = models.Task.objects.filter(pk=id).first()
	return render(req, 'task/edit.html', {
		'data': tasks,
		})

# buat delet
def delete(req, id): #delete fungsi
	task = models.Task.objects.filter(pk=id).delete() #variabel task
	return redirect('/')

