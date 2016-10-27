from django.contrib import admin
from .models import Carrera, Valoracion, Usuario

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Valoracion)
admin.site.register(Usuario)