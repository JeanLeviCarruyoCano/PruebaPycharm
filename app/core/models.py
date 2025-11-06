from django.db import models

# Create your models here.
from django.db import models

class Pais_Carruyo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Estudiante_Jean(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    pais = models.ForeignKey(Pais_Carruyo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre