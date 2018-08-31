from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product 
from .utils import get_cart_items

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', [])
    context = get_cart_items(cart)
    return render(request, "cart/view_cart.html", context)
  

def add_to_cart(request):
    product_id = request.POST['id']
    cart = request.session.get('cart', [])
    cart.append(product_id) 
    request.session['cart'] = cart
    return redirect('product_list')

def remove_cart(request):
    id = request.POST['id']
    cart = request.session.get('cart', [])
    cart.remove(id)
    request.session['cart'] = cart
    return redirect('view_cart')