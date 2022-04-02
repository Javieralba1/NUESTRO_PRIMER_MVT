from statistics import mode
from django.db import models

# Create your models here.
class Mama(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.CharField(max_length=2)

class Hermano(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.CharField(max_length=2)

class Hermana(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.CharField(max_length=2)    

class Novia(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.CharField(max_length=2)

class Mascota(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.CharField(max_length=2)
    raza=models.CharField(max_length=40)    