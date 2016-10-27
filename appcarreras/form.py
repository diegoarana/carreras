from django import forms
from appcarreras.models import Carrera, Valoracion

class ValoraForm(forms.ModelForm):
	class Meta:
		model=Valoracion
		fields=['nombre','cursando','pros','contras','recomendacion','calificacion']

class CarreraForm(forms.ModelForm):
	class Meta:
		model=Carrera
		fields="__all__"