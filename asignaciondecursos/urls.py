from django.urls import path
from .import views 

app_name="asignaciondecursos"

urlpatterns = [
    
    path("agregar/<int:curso_id>/", views.agregar_curso, name="agregar"),
    path("eliminar/<int:curso_id>/", views.eliminar_curso, name="eliminar"),
    path("restar/<int:curso_id>/", views.restar_curso, name="restar"),
    path("limpiar/", views.limpiar_asignaciondecursos, name="limpiar"),
    #path('pago_exitoso', views.pago_exitoso, name='pago_exitoso'),
]
