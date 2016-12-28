"""proyecto_carreras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from carreras import views
from . import views as proyecto_carreras
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', proyecto_carreras.homepage, name='homepage'),
    url(r'^valoraciones/$', views.lista_valoraciones, name='lista_valoraciones'),
    url(r'^valoraciones/eliminar(?P<valorar_id>[0-9]+)/$', views.eliminar_valoracion, name='eliminar_valoracion'),
    url(r'^valoraciones/detalle/(?P<val_id>[0-9]+)/$', views.detalle_valoracion, name='detalle_valoracion'),
    url(r'^registrar/$', proyecto_carreras.registrar, name='registrar'),
    url(r'^login/$', proyecto_carreras.login_page, name='login_page'),
    url(r'^logout/$', proyecto_carreras.logout_page, name='logout_page'),
    url(r'^carreras/', include([
        url(r'^$', views.lista_carreras, name='lista_carreras'),
        url(r'^crear/$', views.crear_carrera, name='crear_carrera'),
        url(r'^(?P<url_carrera>[\w]+)/$', views.detalle_carrera, name='detalle_carrera'),
        url(r'^(?P<url_carrera>[\w]+)/valorar/$', views.valorar_carrera, name='valorar_carrera'),
        url(r'^(?P<url_carrera>[\w]+)/valorar/editar(?P<pk>[0-9]+)/$', views.valorar_editar, name='valorar_editar'),
    ])),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

