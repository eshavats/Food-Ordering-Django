from django.shortcuts import render, redirect
from .models import Food

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def home(request):
    return render(request,"home.html")

def menu(request):
    if(request.method == "GET"):
        foods = Food.objects.all()
    return render(request,"menu.html", {'foods': foods})

def cart(request):
    return render(request,"cart.html")