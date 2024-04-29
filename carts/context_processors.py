from carts.views import _cart_id
from .models import Cart, CartItem

def cart(request):
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            total = 0
            count = 0
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                count += cart_item.quantity
        except Exception as e:
            total = 0
            count = 0
            cart_items = 0
        context = {
            'total': total,
            'count': count,
            'cart_items': cart_items
        }
        return context