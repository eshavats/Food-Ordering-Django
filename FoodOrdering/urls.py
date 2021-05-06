from django.urls import path,include
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.welcome, name="Welcome"),
    path('home/', views.home, name="Home"),
    path('menu/', views.menu, name="Menu"),
    path('cart/', views.cart, name="Cart"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('signupUser/', views.signupUser),
    path('loginUser/', views.loginUser),
    path('logout/',views.logout),
    path('admin/',views.admin),
    path('addhotel/',views.addhotel),
    path('addHotel/',views.addHotel),
    path('allMenu/',views.allMenu),
    path('delete/<int:n>/',views.delete,name="delete"),
    path('edit/<int:n>/',views.edit,name="edit")

]
