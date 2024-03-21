from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def front(request):
    return render(request,'front.html')

def home(request):
    return render(request,'home.html')

def south(request):
    return render(request,'south.html')

def north(request):
    return render(request,'north.html')

def tribal(request):
    return render(request,'tribal.html')

def desserts(request):
    return render(request,'desserts.html')
def recipes(request):
    return render(request,'recipes.html')

def login(request):
    return render(request,'login.html')