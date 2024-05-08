from django.shortcuts import redirect, render
from django_countries import countries

from account.forms import AccountForm
from account.models import Account
from django.contrib import messages
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
            messages.success(request, "Account created successfully")
            return redirect("register")
    else:
        form = AccountForm()
        
    context = {
        "countries": countries,
        "form": form
        
    }
    return render(request, "account/register.html", context)


def login(request):
    return render(request, "account/signin.html")


def logout(request):
    return

def forgot_password(request):
    return