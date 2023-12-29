from django.db import models

# Create your models here.

class CategoriaCur(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaCur"
        verbose_name_plural="categoriasCur"

    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaCur, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="estudiante", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"        

