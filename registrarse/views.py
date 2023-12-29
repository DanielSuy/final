from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Estudiantes
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode



# Create your views here.tu

class VRegistro(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registrarse/registrarse.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.save()
            ncui = form.cleaned_data.get('cui')
            img = form.cleaned_data.get("profile_imagen")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(request=request, username=username, password=password)
            login(request, usuario)

            nuevo_usuario = Estudiantes(user=request.user, username=request.user.username, first_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email, cui=ncui, profile_image=img)
            nuevo_usuario.save()

            # Generar token de confirmación
            token = default_token_generator.make_token(usuario)

            # Construir la URL de confirmación
            confirm_url = f"http://{request.get_host()}/confirmar/{urlsafe_base64_encode(force_bytes(usuario.pk))}/{token}/"

            # Enviar correo de confirmación
            enviar_mail_registro(request, username, request.user.email, confirm_url)


            return redirect('Estudiante')
        else:
            for field_name, error_messages in form.errors.items():
                for msg in error_messages:
                    messages.error(request, f"{field_name}: {msg}")

            return render(request, "registrarse/registrarse.html", {"form": form})
        
        
def cerrar_session(request):
    logout(request)

    return redirect("Estudiante")

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra, request=request)
            if usuario is not None:
                login(request, usuario)
                return redirect("Estudiante")
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")

    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})

def enviar_mail_registro(request, username, email, confirm_url):
    asunto = "Registro Exitoso"
    mensaje = render_to_string("registrarse/email_registro.html", {
        "nombreusuario": username,
        "confirm_url": confirm_url
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "abch428@gmail.com"  # correo de la tienda

    send_mail(asunto, mensaje_texto, from_email, [email], html_message=mensaje)

def perfil (request):
    #Obtener el usuario actual 
    user=request.user

    return render(request, 'perfil/perfil.html')
    