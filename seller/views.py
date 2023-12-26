from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product, Seller, Condition, Category, Offer, Order, Transaction, Rating, Message, Price, Amount, Order_date, Order_status, Status, Payment_method, Quantity, Payment, Buyer, Transaction_status



@login_required
def dashboard(request):
    name = Product.objects.all()

    

    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})

   

def login(request):
    return render(request, 'registration/login.html', {'section': 'login'})


def logout(request):
    return render(request, 'registration/logout.html', {'section': 'logout'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'user_form': user_form})




def password_change_done(request):
    return render(request, 'registration/password_change_done.html')


def password_reset(request):
    return render(request, 'registration/password_reset.html')