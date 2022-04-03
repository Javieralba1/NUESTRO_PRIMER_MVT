from aiohttp import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Incio(request):
    return render(request,"AppCoder/Inicio.html")
def Mama(request):
    return render(request,"AppCoder/Mama.html")
def Hermana(request):
    return render(request,"AppCoder/Hermana.html")
def Hermano(request):
    return render(request,"AppCoder/Hermano.html")
def Mascota(request):
    return render(request,"AppCoder/Mascota.html")
def Novia(request):
    return render(request,"AppCoder/Novia.html")
