from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from carreras.models import Carrera, Valoracion, Usuario
from carreras.form import ValoraForm, CarreraForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, Http404

# Create your views here.
def lista_carreras (request):
	carreras = Carrera.objects.order_by('nombre')
	return render(request, 'carreras/lista_carreras.html', {'carreras': carreras})

def detalle_carrera (request, url_carrera):
	carrera = get_object_or_404(Carrera, url=url_carrera)
	total = carrera.valor_total()
	return render(request, 'carreras/detalle_carrera.html', {'carrera':carrera, 'total':total})

@login_required
def valorar_carrera(request, url_carrera):
	carrera = get_object_or_404(Carrera, url=url_carrera)
	if request.method == 'POST':
		form = ValoraForm(request.POST)
		if form.is_valid():
			valorar = form.save(commit=False)
			valorar.carrera = carrera
			valorar.usuario = request.user.usuario
			valorar.nombre = request.user.username
			valorar.save();
			return redirect('detalle_carrera', url_carrera)
	else:
		form = ValoraForm()
	return render(request, 'carreras/valorar_carrera.html', {'form':form, 'carrera':carrera})

@login_required
def lista_valoraciones(request):
	try:
		lista_val = request.user.usuario.valoracion_set.all()
	except:
		 raise Http404("No hay datos cargados")
	return render(request, 'carreras/lista_valoraciones.html', {'lista_val':lista_val} )


@login_required
def valorar_editar(request, url_carrera, valorar_id):
	carrera = get_object_or_404(Carrera, url=url_carrera)
	valorar = get_object_or_404(carrera.valoracion_set, pk=valorar_id)
	if request.method == 'POST':
		form = ValoraForm(request.POST, instance=valorar)
		if form.is_valid:
			form.save()
			return redirect('detalle_carrera', url_carrera)
	else:
			form = ValoraForm(instance=valorar)
	return render(request, 'carreras/valorar_editar.html', {'form':form, 'carrera':carrera, 'valorar':valorar})

@login_required
def crear_carrera(request):
	if request.method == "POST":
		form = CarreraForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('lista_carreras')
	else:
		form = CarreraForm()
	return render(request, 'carreras/crear_carrera.html', {'form':form})

def carreras_json(request):
	carreras = Carrera.objects.order_by('nombre')
	data = []
	for car in carreras:
		data.append(car.to_dict())		
	return HttpResponse(data, content_type='application/json')

"""def carreras_json(request):
    carreras = Carrera.objects.all()
    data = serializers.serialize("json", carreras)
    return HttpResponse(data, content_type='application/json')"""

