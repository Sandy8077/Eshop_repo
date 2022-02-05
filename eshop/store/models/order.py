from django.db import models
from.product import Product
from.customer import Customer
import datetime

class Order(models.Model):
    product=models.ForeignKey(Product,
                              on_delete=models.CASCADE, null=True)
    customer=models.ForeignKey(Customer,
                              on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1 ,null=True)
    price=models.IntegerField()
    address=models.CharField(max_length=300,
                              default="",blank=True)
    phone=models.CharField(max_length=20,
                           default="",blank=True, null=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)




    def placeOrder(self):
        self.save()


    @staticmethod
    def get_order_by_customers(customer_id):

        return Order.objects.filter(customer=customer_id). order_by('-date')
