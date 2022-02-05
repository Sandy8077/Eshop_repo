from django.contrib import admin
from.models.product import Product
from.models.category import Cetegory
from.models.customer import Customer
from.models.order import Order

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category','description']


class AdminCetegory(admin.ModelAdmin):
        list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name','phone_no','email','password']

class OrderAdmin(admin.ModelAdmin):
    list_display=['product','customer','quantity','price','address','phone','date','status' ]

admin.site.register(Customer,AdminCustomer)
admin.site.register(Product,AdminProduct)
admin.site.register(Cetegory,AdminCetegory)
admin.site.register(Order,OrderAdmin)
