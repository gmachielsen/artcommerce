from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductSearchForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    search_form = ProductSearchForm()
    return render(request, "products/product_list.html", {'products': products, 'search_form': search_form})


def filter_product_list(request):

    products = Product.objects.all()
    
    if request.GET['formaat'] != 'X':
        products = products.filter(formaat=request.GET['formaat'])
        
    if request.GET['oriëntatie'] != 'X':
        products = products.filter(formaat=request.GET['oriëntatie'])

    search_form = ProductSearchForm()
    return render(request, "products/product_list.html", {'products': products, 'search_form': search_form})

    
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_detail.html", {'product': product})


