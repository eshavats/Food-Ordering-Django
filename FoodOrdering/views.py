from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def home(request):
    if 'email' in request.session:
       return render(request,"home.html")
    else:
        return redirect('/login')
        

def addhotel(request):
    return render(request,"addhotel.html")

def allMenu(request):
    menu = Food.objects.all()
    return render(request, 'allMenu.html',{'menu':menu})


def addHotel(request):
    if request.method == "POST" :
        if request.POST.get('editid') is not None:
            newid = request.POST['editid']
            editmenu = Food.objects.get(id=newid)
            editmenu.name = request.POST['name']
            editmenu.desc = request.POST['desc']
            editmenu.price = request.POST['price']
            editmenu.img = request.POST['img']
            editmenu.save()

            return redirect('/allMenu')

        else:    
            n1 = Food()
            n1.name = request.POST['name']
            n1.desc = request.POST['desc']
            n1.price = request.POST['price']
            n1.img = request.POST['img']
            n1.save()

            return redirect('/allMenu')
    else:
        return redirect('/addMenu')

def admin(request):
    users = User.objects.all()
    return render(request, 'admin.html',{'users':users})
        # id = request.POST["id"]
        # qt = int(request.POST["quantity"])

        # food = Food.objects.get(pk=id)

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def menu(request):
    if 'email' in request.session:
        if(request.method == "GET"):
            foods = Food.objects.all()
            return render(request,"menu.html", {'foods': foods})
        else:
            id = request.POST["id"]
            food = Food.objects.get(pk=id)

            cart = request.session.get("cart")

            if cart:
                quantity = cart.get(id)

                if quantity:
                    cart[id] = quantity+1
                else:
                    cart[id] = 1
            else:
                cart = {}
                cart[id] = 1
            
            request.session["cart"] = cart
            print(cart)
            request.session["msg"] = food.name + " " + "successfully added to cart!"
            return redirect("/menu")
    else:
        return redirect('/login')



def cart(request):
    if 'email' in request.session:
        if(request.method == "GET"):
            cart = request.session.get("cart")
            items = []
            total = 0

            if cart:
                for id in cart:
                    itm = {}
                    food = Food.objects.get(pk=id)

                    itm["id"] = id
                    itm["name"] = food.name
                    itm["price"] = food.price
                    itm["quantity"] = cart[id]

                    total += food.price*cart[id]

                    items.append(itm)

                return render(request, "cart.html", {'items': items, 'total': total})
        else:
            id = request.POST["id"]
            cart = request.session.get("cart")
            del cart[id]
            request.session["cart"] = cart
            print(request.session.get("cart"))
            return redirect("/cart")
        return render(request,"cart.html")
    else:
        return redirect('/login')

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
        elif email == 'admin@gmail.com' and password == 'admin123':
            request.session['email'] = 'admin@gmail.com'
            return redirect('/admin')
        else:
            error_msg = 'Invalid Credentials'
        return render(request, 'login.html' , {'error': error_msg})
    return redirect('login.html')
    
def delete(request,n):
    menu = Food.objects.get(id=n)
    menu.delete()
    return redirect('/allMenu')

def edit(request,n):
    menu = Food.objects.get(id=n)
    return render(request, 'addhotel.html',{'menu':menu})
        # id = request.POST["id"]
        # cart = request.session.get("cart")
        # del cart[id]
        # request.session["cart"] = cart
        # return redirect("/cart")
