from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Cetegory
from django.views import View

# Create your views here.
#index



class Index(View):
    def post(self,request):
        print("yaha pahucha mamala")



        try:
            product=request.POST.get("product")
            print(" try ka mamalayaha pahucha")


        except :
            print("null fekra bhai")

        remove=request.POST.get("remove")
        print('product id=',product)
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1

                else:
                    cart[product]=quantity+1


            else:
                cart[product]=1


        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print('cart=',request.session['cart'])
        return redirect("homepage")


    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products=None
        items=Cetegory.get_all_catagary()
        categoryID=request.GET.get('category')
        print(categoryID)
        if categoryID:

             products=Product.get_catagary_id(categoryID)
        else:


            products=Product.Show_product_value()
        data={}
        data['products']=products
        data['items']=items
        print("you are" ,request.session.get('email'))

        return render(request,'index.html',data)
