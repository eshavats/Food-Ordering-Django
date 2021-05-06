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
    else:
        id = request.POST["id"]
        qt = int(request.POST["quantity"])

        food = Food.objects.get(pk=id)

        cart = request.session.get("cart")

        if cart:
            quantity = cart.get(id)

            if quantity:
                cart[id] = quantity+qt
            else:
                cart[id] = qt
        else:
            cart = {}
            cart[id] = qt
        
        request.session["cart"] = cart
        request.session["msg"] = food.name + " " + "successfully added to cart!"
        return redirect("/menu")


def cart(request):
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
                itm["img"] = food.img
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
        return redirect("/cart")