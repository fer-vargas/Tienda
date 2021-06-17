from django.http import request
from django.shortcuts import render

# Create your views here.



def Inicio(request):
    
    return render(request, 'AppMakup/index.html')




def Acerca(request):
    
    return render(request, 'AppMakup/Acerca.html')


def Servicio (requets):
    return render (requets, 'AppMakup/Servicio.html')


def catalogo(request):
    return render(request, 'AppMakup/catalogo.html')


def contacto(request):
    return render(request, 'AppMakup/contacto.html')
