import datetime
import json
from django.shortcuts import redirect, render

from carts.models import CartItem
from orders.forms import OrderForm
from orders.models import Order, Payment, OrderProduct

# Create your views here.

def payments(request):
    # Payment
    body = json.loads(request.body)
    print(body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])
    # Storing transaction details inside Payment Model
    payment = Payment(
        user=request.user,
        payment_id=body['paymentID'],
        payment_method=body['payment_method'],
        amount_paid= order.order_total,
        payer_id=body['payerID'],
        payer_names=body['payerNames'],
        status=body['paymentStatus'],
    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()

    # Move the Cart Items to Order Product Table
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        order_product = OrderProduct()
        order_product.order_id = order.id
        order_product.payment = payment
        order_product.user_id = request.user.id
        order_product.product_id = item.product_id
        order_product.quantity = item.quantity
        order_product.product_price = item.product.price
        order_product.ordered = True
        order_product.save()
        
    # Reduce the quantity of the sold products
    

    # Clear the Cart
   

    # Send order received email to customer


    # Send order number and transaction id back to the client
    data = {
        'order_number': order.order_number,
        'transaction_id': payment.payment_id,
    }
    return render(request, 'orders/payments.html')


def place_order(request, total=0, quantity=0,):
    current_user = request.user

    # If the cart count is less than or equal to 0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total)/100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
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
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            return render(request, 'orders/payments.html', context)
    else:
        return redirect('checkout')


# def create(request):
#     return render(request, 'orders/order_create.html')


# def update(request):
#     return render(request, 'orders/order_update.html')

# def delete(request):
#     return render(request, 'orders/order_delete.html')