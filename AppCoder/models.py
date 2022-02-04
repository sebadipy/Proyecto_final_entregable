from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


    
class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)  
    documento_pac = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.Apellido} - Nro.de documento: {self.documento_pac}'

class Medico(models.Model):
    nombre= models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)  
    Profesion = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.Apellido} - Profesión: {self.Profesion}'

class Practica(models.Model):
    documento_pac = models.IntegerField()
    fecha_practica= models.DateField()
    practica_nombre= models.CharField(max_length=30)

    
    def __str__(self):
        return f'Documento del Paciente: {self.documento_pac} - Práctica: {self.practica_nombre} - Fecha de la práctica: {self.fecha_practica}'

