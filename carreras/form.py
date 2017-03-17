from django import forms
from carreras.models import Carrera, Valoracion

class ValoraForm(forms.ModelForm):
	class Meta:
		model=Valoracion
		fields=['pros','contras','cursando','recomendacion','calificacion']

class CarreraForm(forms.ModelForm):
	class Meta:
		model=Carrera
		fields=['nombre','institucion']

	def __init__(self, *args, **kwargs):
		super(CarreraForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].label = "Nombre de la carrera"
		self.fields['institucion'].label = "Universidad"