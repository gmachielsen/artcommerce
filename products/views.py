from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages
from .forms import ProductSearchForm, ProductSellerForm
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

        products = products.filter(query_by_name | query_by_description)

    
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
    
    if request.GET['kunstenaar']:
        products = products.filter(kunstenaar=request.GET['kunstenaar'])
        
    if request.GET['thema'] != 'X':
        products = products.filter(thema=request.GET['thema'])

    search_form = ProductSearchForm(request.GET)
    return render(request, "products/product_list.html", {'products': products, 'search_form': search_form})

    
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    product_images = ProductImages.objects.filter(product=id)
    return render(request, "products/product_detail.html", {'product': product, 'product_images':product_images})
    

def add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form':form})
        
        
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method=="POST":
        form = ProductSellerForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(profile_seller)
    else:
        form = ProductSellerForm(instance=product)
    
    return render(request, "products/edit_product.html", {'product': product, 'form':form})

# def update_product(form):
#     # Update the DB with the differences
#     if form.is_valid():
#       product = form.save()
#         return redirect("profile_seller") 
#     else:
#           return render(request, "products/edit_product.html", {'product': product, 'form':form})
