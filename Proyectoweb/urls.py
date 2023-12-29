"""
URL configuration for Proyectoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    path('servicios/', include('servicios.urls')),
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('conocenos/', include('conocenos.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('estudiante/', include('estudiante.urls')),
    path('registrarse/', include('registrarse.urls')),
    path('asignaciondecursos/', include('asignaciondecursos.urls')),
    path('asignacion/', include('asignacion.urls')),
    path('docente/', include('docente.urls')),
    path('administrativo/', include('administrativo.urls')),
    path('', include('ProyectoWebApp.urls')),

    
]
