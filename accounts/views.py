from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import BuyerRegistrationForm, SellerRegistrationForm, CardForm
from django.contrib import auth
from django.conf import settings
import stripe
from django.contrib import messages
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

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
        buyer_form = BuyerRegistrationForm()
    return render(request, 'accounts/register_buyer.html', { 'user_form': user_form, 'buyer_form': buyer_form  })

def register_as_seller(request):
    if request.method == 'POST':
        # Load the HTTP Request into two forms, for the User, and the Profile
        user_form = UserCreationForm(request.POST)
        seller_form = SellerRegistrationForm(request.POST)
        card_form = CardForm(request.POST)
        # If both forms are valid, we create the User and Profile in the Database
        if user_form.is_valid() and seller_form.is_valid() and card_form.is_valid():
            # Save the User object to DB, by calling save directly on the Form.
            # Return the User object so that we can use it later to set the user of the Profile.
            user = user_form.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            
            token = card_form.cleaned_data['stripe_id']
            customer = stripe.Customer.create(
                source = token,
                email = "gijs@example.com"
            )
            seller.stripe_id = customer.id
            
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
        seller_form = SellerRegistrationForm() 
        card_form = CardForm()
    return render(request, 'accounts/register_seller.html', { 'user_form': user_form, 'seller_form': seller_form , 'card_form': card_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})

def profile_seller(request):
    products = Product.objects.filter(seller=request.user.seller)
    
    return render(request, 'accounts/profile_seller.html', {'products':products})
    
def subscribe(request):
    
    if request.method == "POST":
        if request.user.seller:
            
            plan = request.POST['plan']
    
            subscription = stripe.Subscription.create(
              customer = request.user.seller.stripe_id,
              items=[{'plan': plan}],
            )
        return redirect('profile_seller')
 
    else:
        return render(request, 'accounts/subscribe.html')
        

