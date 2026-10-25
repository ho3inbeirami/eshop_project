from django.shortcuts import render
from .models import Product

from django.db.models import Avg
# Create your views here.

def product_list(request):
    products_list = Product.objects.all().order_by('-price')
    context = {
        'products_list': products_list,
        'count':Product.objects.count(),
        'AVG':Product.objects.aggregate(Avg('price'))
        }
    return render(request, 'product_module/product_list.html',context=context)



def product_detail(request, slug ):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
        }
    return render(request, 'product_module/product_detail.html',context=context)