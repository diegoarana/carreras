from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your models here.

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")

	def __str__(self):
		return self.user.username

class Carrera (models.Model):
	nombre = models.CharField(blank=False, max_length=30, unique=True)
	institucion = models.CharField(blank=False, max_length=30)
	def __str__(self):
		return self.nombre

	def valor_total(self):
		lista_val = self.valoracion_set.all()
		total = 0
		for val in lista_val:
			total += val.calificacion
		if lista_val.count() != 0:
			total = total / lista_val.count()
		return total

class Valoracion (models.Model):
	carrera = models.ForeignKey(Carrera, null=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
	nombre = models.CharField(max_length=30, blank=False, null=True)
	cursando = models.BooleanField("Cursando actualmente?", default=False)
	pros = models.TextField(blank=False, max_length=100)
	contras = models.TextField(blank=False)
	recomendacion = models.BooleanField("La recomendarias?", default=False)
	calificacion_choices = (
		(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)
		)
	calificacion = models.IntegerField(blank=False, choices=calificacion_choices, default=1)
	fecha_valoracion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre

	def creador_id(self):
		return self.usuario.id		 
	

