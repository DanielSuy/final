from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

"""
class CustomUser(AbstractUser):
    intentos_fallidos = models.IntegerField(default=0)

    # Añadir related_name a los campos de relación
    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        help_text='The groups this user belongs to.', 
        related_name='customuser_groups_set',  # Cambiado el related_name
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_permissions_set',  # Cambiado el related_name
        related_query_name='user'
    )

class Post (models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
"""