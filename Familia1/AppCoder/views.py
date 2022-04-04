from json import load
from re import template
from aiohttp import request
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiares
from django.template import loader
# Create your views here.


def mama(self):
    Mama = Familiares(nombre= "Patricia", apellido = "Albariño", edad ="57", FechaDeNacimiento ="29/09/1964")
    Mama.save(self)
    documentoDetexto = f"Nombre: {Mama.nombre}  Apellido:  {Mama.apellido}  Edad:  {Mama.edad}  Fecha de Nacimiento: {Mama.FechaDeNacimiento}" 
    dicc = {'Mama': Mama}
    template = loader.get_template('AppCoder/Mama.html')
    Documento = template.render(dicc)
    return HttpResponse(Documento)

def Hermano(self):
    Hermano = Familiares(nombre= "Matias", apellido = "Albariño", edad ="35", FechaDeNacimiento ="20/04/1986")
    Hermano.save(self)
    documentoDetexto = f"Nombre: {Hermano.nombre}  Apellido:  {Hermano.apellido}  Edad:  {Hermano.edad}  Fecha de Nacimiento: {Hermano.FechaDeNacimiento}" 
    dicc = {'Hermano': Hermano}
    template = loader.get_template('AppCoder/Hermano.html')
    Documento = template.render(dicc)
    return HttpResponse(Documento)
def Hermana(self):
    Hermana = Familiares(nombre= "Jimena", apellido = "Albariño", edad ="27", FechaDeNacimiento ="16/03/1995")
    Hermana.save(self)
    documentoDetexto = f"Nombre: {Hermana.nombre}  Apellido:  {Hermana.apellido}  Edad:  {Hermana.edad}  Fecha de Nacimiento: {Hermana.FechaDeNacimiento}" 
    dicc = {'Hermana': Hermana}
    template = loader.get_template('AppCoder/Hermana.html')
    Documento = template.render(dicc)
    return HttpResponse(Documento)
