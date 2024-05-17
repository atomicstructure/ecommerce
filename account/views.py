from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django_countries import countries

from account.forms import AccountForm
from account.models import Account
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from carts.models import Cart, CartItem
from carts.views import _cart_id
# Create your views here.


def register(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            phone_number = form.cleaned_data.get("phone_number")
            password = form.cleaned_data.get("password")
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, password=password, username=username)
            user.phone_number = phone_number
            user.username = f"{username}_{user.id}"
            user.save()

            # User Activation
            current_site = get_current_site(request)
            mail_subject = "Please activate your account"
            message = render_to_string("account/activation_email.html", {
                "user": user,
                "domain": current_site,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, "Thank you for registering. We have sent an activation email to the registered email. Please click on the activation link to activate your account.")
            return redirect("/account/login/?command=verification&email="+email)
    else:
        form = AccountForm()
        
    context = {
        # "countries": countries,
        "form": form
        
    }
    return render(request, "account/register.html", context)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    #  Getting the product variation by Cart ID
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                    # Get the Cart Items from the user to access his product variations
                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
    return render(request, "account/signin.html")

@login_required(login_url="login")
def logout(request):
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("login")
    

def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset Password Email
            current_site = get_current_site(request)
            mail_subject = "Reset your password"
            message = render_to_string("account/reset_email_password.html", {
                "user": user,
                "domain": current_site,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address')
            return redirect('login')

        else:
            messages.error(request, 'That email address is not in our database!')
            return redirect('forgotpassword')
    return render(request, 'account/forgot_password.html')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Account activated successfully")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid")
        return redirect('register')
    

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, "Please reset your password")
        return redirect('resetpassword')
    else:
        messages.error(request, "This link has expired")
        return redirect('login')
    

def resetpassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, "Password reset successful")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('resetpassword')
    else:
        return render(request, 'account/reset_password.html')

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'account/dashboard.html')