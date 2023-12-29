from django.contrib import admin
from .models import Conocenos

#Registra tus modelos aqui 

class ConocenosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Conocenos, ConocenosAdmin)
