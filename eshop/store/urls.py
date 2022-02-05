from django.contrib import admin
from django.urls import path
from.import views
from.views import login,home,signup,cart,checkout,orders
from store.middlewares.auth import Auth_Middleware


urlpatterns = [
    path('',views.home.Index.as_view(),name='homepage' ),
    path('signup/',signup.Signup.as_view() ,name='signup' ),
    path('login/',login.Login.as_view() , name='login' ),
    path('logout/',login.logout , name='logout' ),
    path('cart/',cart.Cart.as_view() , name='cart' ),
    path('check_out/',checkout.Checkout.as_view() , name='Checkout' ),
    path('orders/', Auth_Middleware(orders.OrderView.as_view()), name='orders' ),






]
