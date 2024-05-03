from django.shortcuts import render
from django_countries import countries

from account.forms import AccountForm
# Create your views here.


def register(request):
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