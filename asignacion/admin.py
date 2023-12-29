from django.contrib import admin
from .models import Asignacion, LineaAsignacion

# Register your models here.

admin.site.register([Asignacion, LineaAsignacion])
