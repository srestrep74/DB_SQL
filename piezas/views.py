from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def login(request):
    return render(request, 'registration/login.html')

def register(request):
    pass

def home(request):
    return render( request, 'pages/home.html')

def create(request):
    return render(request, 'pages/piece/create.html')

def update(request):
    return render(request, 'pages/piece/update.html')

def mycollection(request):
    return render(request, 'pages/mycollection.html')

def infopiece(request):
    return render(request, 'pages/infopiece.html')