from django.shortcuts import get_object_or_404
from products.models import Product

def get_cart_items(cart):
    total = 0
    cart_items = []
    for product_id in cart:
        product = get_object_or_404(Product, pk=product_id)
        total += product.price
        cart_items.append({'product':product})

    return {'cart_items': cart_items, 'total': total}
    