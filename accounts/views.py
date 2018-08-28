from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import BuyerRegistrationForm, SellerRegistrationForm
from django.contrib import auth

def register_as_customer(request):
    if request.method == 'POST':
        # Load the HTTP Request into two forms, for the User, and the Profile
        user_form = UserCreationForm(request.POST)
        customer_form = BuyerRegistrationForm(request.POST)

        # If both forms are valid, we create the User and Profile in the Database
        if user_form.is_valid() and customer_form.is_valid():
            # Save the User object to DB, by calling save directly on the Form.
            # Return the User object so that we can use it later to set the user of the Profile.
            user = user_form.save()
            buyer = customer_form.save(commit=False)
            buyer.user = user
            buyer.save()
            
            # Now we can log in as the new user 
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")

            return redirect('home')
    else:
        user_form = UserCreationForm()
        customer_form = BuyerRegistrationForm()
    return render(request, 'accounts/register.html', { 'user_form': user_form, 'user_type_form': customer_form })

def register_as_seller(request):
    if request.method == 'POST':
        # Load the HTTP Request into two forms, for the User, and the Profile
        user_form = UserCreationForm(request.POST)
        seller_form = SellerRegistrationForm(request.POST)
        # If both forms are valid, we create the User and Profile in the Database
        if user_form.is_valid() and seller_form.is_valid():
            # Save the User object to DB, by calling save directly on the Form.
            # Return the User object so that we can use it later to set the user of the Profile.
            user = user_form.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            seller.save()
            
            # Now we can log in as the new user 
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
                
            return redirect('home')
    else:
        user_form = UserCreationForm()
        user_type_form = SellerRegistrationForm()
    return render(request, 'accounts/register.html', { 'user_form': user_form, 'user_type_form': user_type_form })



