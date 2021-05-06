from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def home(request):
    return render(request,"home.html")

def menu(request):
    return render(request,"menu.html")

def cart(request):
    return render(request,"cart.html")