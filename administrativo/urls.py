from django.urls import path
from django.contrib import admin
from django.urls import path 
from .import views 

urlpatterns = [
    
    path('',views.administrativo, name='Administrativo'),
    path('admin/', admin.site.urls, name='Admin'),
    
]






    