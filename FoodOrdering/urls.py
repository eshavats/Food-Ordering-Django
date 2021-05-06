from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.welcome, name="Welcome"),
    path("home", views.home, name="Home"),
    path('menu', views.menu, name="Menu"),
    path("cart", views.cart, name="Cart")
]
