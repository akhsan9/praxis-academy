from django.shortcuts import render, redirect

from . import models, forms


def index(req): # 
	
	tasks = models.Task.objects.all() # ditampung di Variabel tasks
	# fields = ('name', 'telp', 'seri', 'country', 'kerusakan', 'status')
	return render(req, 'task/index.html', 
		{ 'data': tasks, 
		})  

def create(req):
	form_input = forms.TaskForm()
	if req.POST:
		form_input = forms.TaskForm(req.POST)
		if form_input.is_valid():
			form_input.save()
			return redirect('/app/')

	return render(req, 'task/create.html', 
		{ 
		'form': form_input,
		})

def detail(req, id):	
	task = models.Task.objects.filter(pk=id).first() # model first
	return render(req, 'task/detail.html',
		{ 'data': task,
		}) 

#	Membuat 'Edit'

def edit(req, id):
	if req.POST:
		models.Task.objects.filter(pk=id).update(
			name=req.POST['name'],
			telp=req.POST['telp'],
			seri=req.POST['seri'],
			country=req.POST['country'],
			kerusakan=req.POST['kerusakan'],
			status=req.POST['status'])
		return redirect('/app')

	tasks = models.Task.objects.filter(pk=id).first()
	return render(req, 'task/edit.html', {
		'data': tasks,
		})

# buat delet
def delete(req, id): #delete fungsi
	task = models.Task.objects.filter(pk=id).delete() #variabel task
	return redirect('/app')

