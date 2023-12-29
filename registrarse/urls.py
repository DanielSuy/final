from django.urls import path
from .views import VRegistro, cerrar_session, logear, enviar_mail_registro 
from .views import perfil
from registrarse import views


urlpatterns = [
    
    path('',VRegistro.as_view(), name='Registrarse'),
    path('cerrar_session',cerrar_session, name='cerrar_session'),
    path('logear',logear, name='logear'),
    #path('procesar_registro', procesar_registro, name='procesar_registro' ),
    path('enviar_mail_registro', enviar_mail_registro, name='enviar_mail_registro' ),
    path('perfil',views.perfil, name='perfil'),    

]

