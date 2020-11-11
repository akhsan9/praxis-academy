
from django.shortcuts import render, redirect
from . import models, forms

def index(req):
	home = models.Homer.objects.all()
	return render(req, 'home/index.html',
	{
		'data': home,
	})

def tambah(req):
	form_input = forms.HomeForm()
	if req.POST:
		form_input = forms.HomeForm(req.POST)
		if form_input.is_valid():
			form_input.save()
			return redirect('/')

	return render(req, 'home/tambah.html', 
		{ 
		'form': form_input,
		})

def detaile(req, id):
	task = models.Homer.objects.filter(id=id)
	return render(req, 'home/detaile.html', 
	{
		'task': task,
	})

def edited(req, id):
	if req.POST:
		models.Homer.objects.filter(pk=id).update(
			nama=req.POST['nama'],
			telpon=req.POST['telpon'],
			kota=req.POST['kota'],
			statuses=req.POST['statuses'])
		return redirect('/')

	tasks = models.Homer.objects.filter(pk=id).first()
	return render(req, 'home/edit.html', {
		'data': tasks,
		})

def delete(req, id): 
	task = models.Homer.objects.filter(pk=id).delete()
	return redirect('/')

