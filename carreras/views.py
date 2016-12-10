from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from carreras.models import Carrera, Valoracion, Usuario
from carreras.form import ValoraForm, CarreraForm
from carreras.permission import is_owner_permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def lista_carreras (request):
	carreras = Carrera.objects.order_by('nombre')
	return render(request, 'carreras/lista_carreras.html', {'carreras': carreras})

def detalle_carrera (request, url_carrera):
	carrera = get_object_or_404(Carrera, url=url_carrera)
	total = carrera.valor_total()
	lista_val = carrera.valoracion_set.all()

	paginator = Paginator(lista_val, 3) # Show 3 valorations per page
	page = request.GET.get('page')
	try:
		lista_val = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		lista_val = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		lista_val = paginator.page(paginator.num_pages)
	
	return render(request, 'carreras/detalle_carrera.html', {'lista_val':lista_val, 'total':total})
	#hace falta modificar el template ya que le estoy pasando la lista reducida de objetos y no todas las valoraciones

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
def eliminar_valoracion(request, valorar_id):
	valo = get_object_or_404(Valoracion, pk=valorar_id)
	valo.delete()
	return redirect('homepage')
	

@login_required
@is_owner_permission_required(Valoracion)
def valorar_editar(request, url_carrera, pk):
	carrera = get_object_or_404(Carrera, url=url_carrera)
	valorar = get_object_or_404(carrera.valoracion_set, pk=pk)
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
