from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your models here.

def remove_spaces(value):
    return value.replace(' ', '')

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")

	def __str__(self):
		return self.user.username

class Carrera (models.Model):
	nombre = models.CharField(blank=False, max_length=30, unique=True)
	institucion = models.CharField(blank=False, max_length=30)
	url = models.CharField(max_length=100, null=True)
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

	def save(self, *args, **kwargs):
		self.url = remove_spaces(self.nombre)
		super(Carrera, self).save(*args, **kwargs)

	def to_dict(self):
		result = {
		"id": self.id,
		"nombre": self.nombre,
		"institucion": self.institucion
		}
		return result

class Valoracion (models.Model):
	carrera = models.ForeignKey(Carrera, null=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	cursando = models.BooleanField("Cursando actualmente?", default=False)
	pros = models.TextField(blank=False, max_length=100)
	contras = models.TextField(blank=False)
	recomendacion = models.BooleanField("La recomendarias?", default=False)
	calificacion_choices = (
		(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)
		)
	calificacion = models.IntegerField(blank=False, choices=calificacion_choices, default=2)
	fecha_valoracion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre

	def creador_id(self):
		return self.usuario.id

	def is_owner(self, user):
		return self.usuario.user == user

