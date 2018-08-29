from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductSearchForm
from django.db.models import Q

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    search_form = ProductSearchForm()
    return render(request, "products/product_list.html", {'products': products, 'search_form': search_form})


def filter_product_list(request):


    products = Product.objects.all()
    

    if 'search' in request.GET:
        search = request.GET['search']
        
        query_by_name = Q(name__contains=search)
        query_by_description = Q(description__contains=search)
        query_by_kunstenaar = Q(kunstenaar__contains=search)
        
        products = products.filter(query_by_name | query_by_description | query_by_kunstenaar)

    
    if request.GET['formaat'] != 'X':
        products = products.filter(formaat=request.GET['formaat'])


    if request.GET['oriëntatie'] != 'X':
        products = products.filter(oriëntatie=request.GET['oriëntatie'])
    

    if request.GET['techniek'] != 'X':
        products = products.filter(techniek=request.GET['techniek'])
    
    if request.GET['prijs'] != 'X':
        products = products.filter(prijs=request.GET['prijs'])
        
    if request.GET['prijstype'] != 'X':
        products = products.filter(prijstype=request.GET['prijstype'])
    
    if request.GET['stijl'] != 'X':
        products = products.filter(stijl=request.GET['stijl'])
    
    if request.GET['stijl'] != 'X':
        products = products.filter(kunstenaar=request.GET['kunstenaar'])

    search_form = ProductSearchForm()
    return render(request, "products/product_list.html", {'products': products, 'search_form': search_form})

    
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_detail.html", {'product': product})


