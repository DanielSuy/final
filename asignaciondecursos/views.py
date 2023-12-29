from django.shortcuts import redirect
from .asignaciondecursos import Asignaciondecursos
from estudiante.models import Curso

# Create your views here.

def agregar_curso(request, curso_id):

    asignaciondecursos=Asignaciondecursos(request)
    curso=Curso.objects.get(id=curso_id)
    asignaciondecursos.agregar(curso=curso)
    return redirect("Estudiante")

def eliminar_curso(request, curso_id):

    asignaciondecursos=Asignaciondecursos(request)
    curso=Curso.objects.get(id=curso_id)
    asignaciondecursos.eliminar(curso=curso)
    return redirect("Estudiante")


def restar_curso(request, curso_id):
    asignaciondecursos=Asignaciondecursos(request)
    curso=Curso.objects.get(id=curso_id)
    asignaciondecursos.restar_curso(curso=curso)
    return redirect("Estudiante")


def limpiar_asignaciondecursos(request, curso_id):
    asignaciondecursos=Asignaciondecursos(request)
    asignaciondecursos.limpiar_asignaciondecursos()
    return redirect("Estudiante")
