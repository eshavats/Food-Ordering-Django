from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def home(request):
    return render(request,"home.html")

def addhotel(request):
    return render(request,"addhotel.html")

def admin(request):
    users = User.objects.all()
    return render(request, 'admin.html',{'users':users})

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def menu(request):
    return render(request,"menu.html")

def cart(request):
    return render(request,"cart.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('/home')

def signupUser(request):
    if request.method == 'POST':
        error_msg = None
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            error_msg = 'Email id already exists'
            return render(request, 'signup.html' , {'error': error_msg})
        else:
            u1 = User()
            u1.name = request.POST['name']
            u1.contact = request.POST['contact']
            u1.email = request.POST['email']
            u1.password = request.POST['password']
            u1.gender = request.POST['gender']
            u1.save()
            request.session['email'] = request.POST['email']  
        return redirect('/menu')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_msg = None
        if User.objects.filter(email=email,password=password).exists():
            request.session['email'] = email
            return redirect('/home')
        elif email == 'admin@gmai.com' and password == 'admin123':
            return redirect('/admin')
        else:
            error_msg = 'Invalid Credentials'
        return render(request, 'login.html' , {'error': error_msg})
    return redirect('login.html')
