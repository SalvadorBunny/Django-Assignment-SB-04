from django.db import models
from django.urls import reverse

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('list_client')