from django.shortcuts import render, redirect

from . import models, forms

def index(req):
	data = models.Barang.objects.all()
	return render(req, 'barang/index.html',
	{
		'data': data,
	})

def tambah(req):
	form_input = forms.BarangForm()
	if req.POST:
		form_input = forms.BarangForm(req.POST)
		if form_input.is_valid():
			form_input.save()
			return redirect('/barang')

	return render(req, 'barang/tambah.html', 
		{ 
		'form': form_input,
		})

def detil(req, id):	
	task = models.Barang.objects.filter(pk=id).first() # model first
	return render(req, 'barang/detil.html',
		{ 'data': task,
		}) 

def edit(req, id):
	if req.POST:
		models.Barang.objects.filter(pk=id).update(
			names=req.POST['names'],
			series=req.POST['series'],
			stok=req.POST['stok'],
			# status=req.POST['status']
			)
		return redirect('/barang')

	tasks = models.Barang.objects.filter(pk=id).first()
	return render(req, 'barang/edit.html', {
		'data': tasks,
		})


# buat delet
def delete(req, id): #delete fungsi
	task = models.Barang.objects.filter(pk=id).delete() #variabel task
	return redirect('/barang')

