from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.db import models
from django.views import View
from store.models.product import Product
from store.models.order import Order
from store.middlewares.auth import Auth_Middleware













class OrderView(View):


    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_order_by_customers(customer)
        print(orders)
        return render(request,'order.html',{'orders':orders})
