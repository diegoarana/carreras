from django.shortcuts import render, get_object_or_404, redirect
from appcarreras.models import Carrera, Valoracion
from appcarreras.form import ValoraForm, CarreraForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def lista_carreras (request):
	carreras = Carrera.objects.order_by('nombre')	
	return render(request, 'appcarreras/lista_carreras.html', {'carreras': carreras})

def detalle_carrera (request, carrera_id):
	carrera = get_object_or_404(Carrera, pk=carrera_id)
	lista_val = carrera.valoracion_set.all()
	total = 0
	for val in lista_val:
		total += val.calificacion
	if lista_val.count() != 0:
		total = total / lista_val.count()
	return render(request, 'appcarreras/detalle_carrera.html', {'carrera':carrera, 'total':total})

@login_required
def valorar_carrera(request, carrera_id):
	carrera = get_object_or_404(Carrera, pk=carrera_id)
	if request.method == 'POST':
		form = ValoraForm(request.POST)
		if form.is_valid():
			valorar = form.save(commit=False)
			valorar.carrera = carrera
			valorar.save();
			return redirect('detalle_carrera', carrera_id)
	else:
		form = ValoraForm()
	return render(request, 'appcarreras/valorar_carrera.html', {'form':form, 'carrera':carrera})

@login_required
def valorar_editar(request, carrera_id, valorar_id):
	carrera = get_object_or_404(Carrera, pk=carrera_id)
	valorar = get_object_or_404(carrera.valoracion_set, pk=valorar_id)
	if request.method == 'POST':
		form = ValoraForm(request.POST, instance=valorar)
		if form.is_valid:
			form.save()
			return redirect('detalle_carrera', carrera_id)
	else:
			form = ValoraForm(instance=valorar)
	return render(request, 'appcarreras/valorar_editar.html', {'form':form, 'carrera':carrera, 'valorar':valorar})

@login_required
def crear_carrera(request):
	if request.method == "POST":
		form = CarreraForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('lista_carreras')
	else:
		form = CarreraForm()
	return render(request, 'appcarreras/crear_carrera.html', {'form':form})

def carreras_json(request):
    carreras = Carrera.objects.all()
    data = serializers.serialize("json", carreras)
    return HttpResponse(data, content_type='application/json')