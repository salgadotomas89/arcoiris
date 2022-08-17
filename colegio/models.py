from django.db import models
from django.utils import timezone


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, default=" ")
    lead = models.CharField(max_length=1000, default=" ")
    texto = models.CharField(max_length=1000, default='SOME ')
    documento = models.FileField(upload_to='noticias')
    date = models.DateTimeField(default=timezone.now)
    redactor = models.CharField(max_length=200, default='Tomás Salgado')
    tituloDestacado = models.CharField(max_length=100, default=" ")
    destacado = models.CharField(max_length=1000, default="")


class Evento(models.Model):
    fecha = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    texto = models.CharField(max_length=600)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    ciclo = models.IntegerField(default=3)
    universidad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default='profesor')
    foto = models.ImageField(upload_to='profesores')


class Colegio(models.Model):
    nombre = models.CharField(max_length=200)
    mision = models.CharField(max_length=200)
    vision = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fono = models.CharField(max_length=200)
    funciones = models.BooleanField()