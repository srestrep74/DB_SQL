from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import pieza


def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')

def home(request):
    return render( request, 'pages/home.html')

def create(request):
    formulario = pieza(request.POST or None)
    return render(request, 'pages/piece/create.html', {'formulario':formulario})

def update(request):
    formulario = pieza(request.POST or None)
    return render(request, 'pages/piece/update.html', {'formulario' : formulario})

def mycollection(request):
    return render(request, 'pages/mycollection.html')

def buy(request):
    return render(request, 'pages/buy.html')