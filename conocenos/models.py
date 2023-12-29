from django.db import models

# Create your models here.

class Conocenos(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=1000)
    imagen=models.ImageField(upload_to='conocenos')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='conocenos'
        verbose_name_plural='conocenos'

    def __str__(self):
        return self.titulo