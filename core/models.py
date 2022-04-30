import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashlib import md5
from DarkMatterMaytok.settings import USER_RANK


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
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre')
    rank = models.CharField(max_length=50, choices=USER_RANK, default='0')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=True, verbose_name='Email')
    is_founder = models.BooleanField(default=False)
    is_founder_emailed = models.BooleanField(default=False)
    guid = models.UUIDField(null=True, blank=True, default=uuid.uuid4)
    balance = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.get_full_name()

    @property
    def get_avatar(self):
        try:
            return self.avatar.url
        except ValueError:
            return f"https://www.gravatar.com/avatar/{md5(self.email.encode('utf-8')).hexdigest()}.jpg?d=identicon"
