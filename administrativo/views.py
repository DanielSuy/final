from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model


# Create your views here.

def administrativo(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra, request=request)

            #if usuario is not None:
                # Verificar si la cuenta está bloqueada
               # if usuario.customuser.intentos_fallidos >= 3:
                    #return HttpResponseForbidden("La cuenta está bloqueada. Por favor, contacta al soporte.")
  
            login(request, usuario)
            es_administrador=request.user.is_superuser
            if es_administrador:                
                admin_url=reverse('admin:index')
                # Restablecer el contador de intentos fallidos
                #usuario.customuser.intentos_fallidos = 0
                #usuario.customuser.save()
                return redirect(admin_url)
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "Contraseña incorrecta")

    form=AuthenticationForm()
    return render(request,"administrativo/administrativo.html",{"form":form})
