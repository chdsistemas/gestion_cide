from django.db import models
from django.contrib.auth.models import AbstractUser


class Rol(models.Model):
    codigo = models.CharField(max_length=10, blank=False, unique=True)
    nombre = models.CharField(max_length=50, unique=True, default='INSTRUCTOR')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    TIPO_DOC = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('OT', 'Otro'),
    ]
    tipo_doc = models.CharField(max_length=2, choices=TIPO_DOC, default='CC')
    numero_doc = models.CharField(max_length=30, unique=True, default='')
    telefono = models.CharField(max_length=30, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT) 

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    
