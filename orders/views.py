import datetime
from django.shortcuts import redirect, render

from carts.models import CartItem
from orders.forms import OrderForm
from orders.models import Order
from decimal import Decimal
# Create your views here.


def place_order(request, total=0, quantity=0):
    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)
    cart_cout = cart_items.count()
    if cart_cout <= 0:
        return redirect('store:store')
    
    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total = cart_item.product.price * cart_item.quantity
        quantity += cart_item.quantity
    tax = Decimal(2 * grand_total) / 100
    grand_total = total + tax
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the order information in the database
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.order_note = form.cleaned_data['order_note']
            data.save()

            # Genrate Order Number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('checkout')
        else:
            return redirect('checkout')


# def create(request):
#     return render(request, 'orders/order_create.html')


# def update(request):
#     return render(request, 'orders/order_update.html')

# def delete(request):
#     return render(request, 'orders/order_delete.html')