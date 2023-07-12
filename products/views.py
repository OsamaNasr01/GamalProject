from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
import pdb

# Create your views here.
def product(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)



def brands(request):
    context = {
        'brands': Brand.objects.all()
    }
    return render(request, 'products/brands.html', context)



def categories(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'products/categories.html', context)




def productdetails(request, slug):

    product = get_object_or_404(Product, slug = slug)
    context = {'product': product}
    return render(request, 'products/product.html', context)