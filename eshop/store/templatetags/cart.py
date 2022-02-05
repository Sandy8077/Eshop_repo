from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
     keys=cart.keys()
     for id in keys:
         a=int(id)
         print("type of a is= ",a)

        
         print("type of id is= ",product.id)
         if a==product.id:
             return True


     return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
        return cart[str(product.id)]




@register.filter(name='price_totel')
def price_totel(product,cart):
     return product.price * cart_quantity(product , cart)

@register.filter(name='totel_cart_price')
def totel_cart_price(products,cart):
    sum=0
    for p in products:
        sum=sum+price_totel(p,cart)
    return sum
