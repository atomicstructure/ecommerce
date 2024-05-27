from django.shortcuts import redirect, render

from carts.models import CartItem
from orders.forms import OrderForm

# Create your views here.


def place_order(request):
    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)
    cart_cout = cart_items.count()
    if cart_cout <= 0:
        return redirect('store:store')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)

def create(request):
    return render(request, 'orders/order_create.html')


def update(request):
    return render(request, 'orders/order_update.html')

def delete(request):
    return render(request, 'orders/order_delete.html')