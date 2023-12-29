from django.urls import path
from .import views 


urlpatterns = [
    
    path('',views.procesar_asignacion, name="procesar_asignacion"),
    #path('generar_factura',views.generar_factura, name="generar_factura"),
    path('enviar_mail',views.enviar_mail, name="enviar_mail"),
    path('index', views.index, name='index'), 
    path('descargar/', views.descargar_archivo, name = "descargar"), 
    path('Pagar', views.procesar_pago, name='Pagar'),
]