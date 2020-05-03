from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Actualizado en')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    GENDERS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    gender = models.CharField(max_length=1, choices=GENDERS, default='M', verbose_name='Género')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Apellidos y nombres')

    class Meta:
        ordering = ['pk']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
