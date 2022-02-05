from django.db import models
from.category import Cetegory

class Product(models.Model):
    name=models.CharField(max_length=50,default='')
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Cetegory,on_delete=models.CASCADE,null=True)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='Uploaded/products/')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)



    @staticmethod
    def Show_product_value():

        prod=Product.objects.all()
        return prod

    @staticmethod
    def get_catagary_id(category_id):
        if category_id:


            return Product.objects.filter(category=category_id)
        else:
            return Product.Show_product_value()
