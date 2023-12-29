from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from asignaciondecursos.asignaciondecursos import Asignaciondecursos
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Asignacion
from asignacion.models import LineaAsignacion, Asignacion
from django.http.response import HttpResponse
from xhtml2pdf import pisa
from estudiante.models import Curso
from .forms import PagoForm
from django.contrib import messages



# Create your views here.
@login_required(login_url="/registrarse/logear")
def procesar_asignacion(request):
    asignacion=Asignacion.objects.create(user=request.user)
    asignaciondecursos=Asignaciondecursos(request)
    lineas_asignacion=list()

    for key, value in asignaciondecursos.asignaciondecursos.items():
        lineas_asignacion.append(LineaAsignacion(
            curso_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            asignacion=asignacion
        ))

    LineaAsignacion.objects.bulk_create(lineas_asignacion)
    enviar_mail(
            asignacion=asignacion,
            lineas_asignacion=lineas_asignacion,
            nombreusuario=request.user.username,
            email_usuario=request.user.email
    )
    messages.success(request, "Su asignacion ha sido exitosa")
    #para que después de procesar el pedido el usuario se quede en la tienda 
    return redirect("perfil") 
    
def enviar_mail(**kwargs):
    asunto="Asignacion Exitosa"
    mensaje=render_to_string("emails/asignacion.html",{
        "asignacion": kwargs.get("asignacion"),
        "lineas_asignacion": kwargs.get("lineas_asignacion"),
        "nombreusuario":kwargs.get("nombreusuario"),
        "importe_total_asignaciondecursos": kwargs.get("importe_total_asignaciondecursos"),
    })
    mensaje_texto=strip_tags(mensaje)
    from_email="abch428@gmail.com" #correo de la tienda 
    to=kwargs.get("email_usuario") #Destinatario
    #to="angyhdez5238@gmail.com" #aca se puede comprobar si funciona el envío de correo, colocar un correo válido

    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)

def importe_total_asignaciondecursos(request):
    total = 0

    # Verificar si la clave 'asignaciondecursos' está presente en request.session
    if hasattr(request, 'session') and 'asignaciondecursos' in request.session:
        for key, value in request.session["asignaciondecursos"].items():
            total += float(value["precio"])
    else:
        total = None

    return {"importe_total_asignaciondecursos": total}

def index(request):
    return render(request, 'perfil.html')

def descargar_archivo(request): 
    filename = 'mis_cursos.pdf' 
    pdf_content = render_to_pdf('factura/listado_cursos.html', {}) # Renderizar el HTML a un objeto BytesIO
    response = HttpResponse(pdf_content, content_type='application/pdf') # Configurar la respuesta HTTP
    response['Content-Disposition'] = f"attachment; filename={filename}" # Configurar las cabeceras para la descarga

    return response

def render_to_pdf(template_path, request):
    
    cursos = Curso.objects.all()
    total = request=request

    context = {
        "cursos": cursos,
        "total": total
    }
    html_content = render_to_string(template_path, context)
    pdf_content = pisa.CreatePDF(html_content)

    return pdf_content.dest.getvalue()

def procesar_pago(request):
    if request.method == 'POST':
        # Recuperar la información del formulario de pago
        form = PagoForm(request.POST)
        if form.is_valid():
            nombre_tarjeta = form.cleaned_data['nombre_tarjeta']
            numero_tarjeta = form.cleaned_data['numero_tarjeta']
            codigo = form.cleaned_data['codigo']

            # Procesar el pago (falso procesador de pago)
            pago_exitoso = procesar_pago_falso(nombre_tarjeta, numero_tarjeta, codigo)

            if pago_exitoso:
                messages.success(request, "SU PAGO HA SIDO EXITOSO")
                return render(request, 'pago_exitoso.html')
                
            
            else:
                messages.error(request, "SU PAGO NO HA SIDO PROCESADO")
                return render(request, 'pago_fallido.html') 

    else:
        form = PagoForm()

    return render(request, 'pago_fallido.html', {'form': form})

def procesar_pago_falso(nombre_tarjeta, numero_tarjeta, codigo):
    return True
