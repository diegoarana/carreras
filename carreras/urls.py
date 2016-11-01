"""carreras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'carreras.views.homepage', name='homepage'),
    url(r'^carreras/$', 'appcarreras.views.lista_carreras', name='lista_carreras'),
    url(r'^carreras/json/$', 'appcarreras.views.carreras_json', name='carreras_json'),
    url(r'^valoraciones/$', 'appcarreras.views.lista_valoraciones', name='lista_valoraciones'),
    url(r'^registrar/$', 'carreras.views.registrar', name='registrar'),
    url(r'^login/$', 'carreras.views.login_page', name='login_page'),
    url(r'^logout/$', 'carreras.views.logout_page', name='logout_page'),
    url(r'^carreras/crear/$', 'appcarreras.views.crear_carrera', name='crear_carrera'),
    url(r'^carreras/(?P<carrera_id>[0-9]+)/$', 'appcarreras.views.detalle_carrera', name='detalle_carrera'),
    url(r'^carreras/(?P<carrera_id>[0-9]+)/valorar/$', 'appcarreras.views.valorar_carrera', name='valorar_carrera'),
    url(r'^carreras/(?P<carrera_id>[0-9]+)/valorar/editar(?P<valorar_id>[0-9]+)/$', 'appcarreras.views.valorar_editar', name='valorar_editar')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
